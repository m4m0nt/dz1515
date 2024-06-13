import random
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.graph_objs as go

x = [i * 0.1 for i in range(-100, 101)]
y = [2 * i + 1 for i in x]

plt.plot(x, y, label='y = 2x + 1')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Graph of y = 2x + 1')

plt.legend()

plt.grid(True)
plt.show()


data = [random.random() for _ in range(1000)]

plt.hist(data, bins=30, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Random Numbers')

plt.grid(True)

plt.show()


categories = ['Movies', 'Concerts', 'Sports', 'Games', 'Others']
percentages = [25, 20, 15, 30, 10]

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(categories)))

fig, ax = plt.subplots()
ax.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%',
       wedgeprops={"linewidth": 1, "edgecolor": "white"})

ax.set_title('Entertainments')

ax.legend(categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()


x_values = [i * 0.1 for i in range(-50, 51)]
y_values = [i * 0.1 for i in range(-50, 51)]

x, y = np.meshgrid(x_values, y_values)

z = np.array([[math.sin(math.sqrt(xi ** 2 + yi ** 2)) for xi in x_values] for yi in y_values])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D z = sin(sqrt(x^2 + y^2))')

plt.show()


x = [i * 0.1 for i in range(-100, 101)]
y = [3 * i + 2 for i in x]

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y = 3x + 2'))

fig.update_layout(
    title='Graph of y = 3x + 2',
    xaxis_title='x',
    yaxis_title='y'
)

fig.show()

import plotly.graph_objs as go
import random
import math


def generate_random_numbers(n):
    numbers = []
    for _ in range(n // 2):
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        numbers.append(z0)
        numbers.append(z1)
    if n % 2 != 0:
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        numbers.append(z0)
    return numbers


data = generate_random_numbers(1000)

fig = go.Figure(data=[go.Histogram(x=data, nbinsx=30)])

fig.update_layout(
    title='Histogram of 1000 Random Numbers',
    xaxis_title='Value',
    yaxis_title='Frequency'
)

fig.show()

x = [i * 0.01 for i in range(int(2 * math.pi / 0.01) + 1)]
y_sin = [math.sin(i) for i in x]
y_cos = [math.cos(i) for i in x]

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y_sin, mode='lines', name='y = sin(x)'))
fig.add_trace(go.Scatter(x=x, y=y_cos, mode='lines', name='y = cos(x)'))

fig.update_layout(
    title='Graphs of y = sin(x) and y = cos(x)',
    xaxis_title='x',
    yaxis_title='y'
)

fig.show()

categories = ['Movies', 'Concerts', 'Sports', 'Games', 'Others']
percentages = [25, 20, 15, 30, 10]

fig = go.Figure(data=[go.Pie(labels=categories, values=percentages, hole=.3)])

fig.update_layout(
    title='Entertainments',
)

fig.show()
