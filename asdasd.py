from datetime import datetime

from pydantic.v1 import BaseModel, root_validator, validator

from typing import List

min_order_amount = 50.0
valid_status = ["new", "processing", "shipped", "delivered"]
status_transition = {
    "new": ["processing", "shipped", "delivered"],
    "processing": ["shipped", "delivered"],
    "shipped": ["delivered"]
}


class Product(BaseModel):
    id: str
    name: str
    category: str
    price: float
    stock_quantity: int


class Customer(BaseModel):
    id: str
    name: str
    email: str
    orders: List['Order'] = []


class OrderItem(BaseModel):
    product: Product
    quantity: int

    @validator('quantity')
    def check_quantity(cls, value, values):
        if 'product' in values and values['product'].stock_quantity < value:
            raise ValueError('Error')
        return value


class Order(BaseModel):
    id: str
    date: datetime
    customer: Customer
    items: List[OrderItem]
    status: str

    @validator('status')
    def check_valid_status(cls, value):
        if value not in valid_status:
            raise ValueError('Error')
        return value

    @root_validator(pre=True)
    def check(cls, values):
        items = values.get('items', [])
        total_amount = sum(item.product.price * item.quantity for item in items)
        if total_amount < min_order_amount:
            raise ValueError(f'Total order amount should be at least {min_order_amount}')

        for item in items:
            item.product.stock_quantity -= item.quantity
        return values

    @validator('status')
    def status(cls, value, values):
        if 'status' in values and values['status'] and values['status'] != value:
            if value not in status_transition.get(values['status'], []):
                raise ValueError(f"Cannot change status from {values['status']} to {value}")
        return value
