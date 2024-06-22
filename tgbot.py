import requests
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.constants import ChatAction
from datetime import datetime, timedelta
import time

API_TOKEN = '7128359513:AAE5FHq30KoTxjpXEqdtQnBd2-pq68xtSuM'
WEATHER_API_KEY = '23bf1a1f1a9e89650f2ed395d4eafe12'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_API_URL = 'http://api.openweathermap.org/data/2.5/forecast'

bot = telebot.TeleBot(API_TOKEN)

user_city = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Please enter your city using /weather (your city)')


@bot.message_handler(commands=['weather'])
def get_weather(message):
    try:
        city = " ".join(message.text.split()[1:])
        user_city[message.chat.id] = city
        markup = ReplyKeyboardMarkup()
        button1 = KeyboardButton('Today')
        button2 = KeyboardButton('Tomorrow')
        button3 = KeyboardButton('3 Days')
        markup.row(button1, button2, button3)
        bot.send_message(message.chat.id, f'Your city is {city}', reply_markup=markup)
    except IndexError:
        bot.send_message(message.chat.id, 'Please provide a city name using /weather <city_name>.')


@bot.message_handler(func=lambda message: message.text.lower() in ('today', 'now'))
def get_weather_today(message):
    city = user_city.get(message.chat.id)
    if city:
        weather_data = fetch_weather(city)
        if weather_data:
            bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            time.sleep(2)
            date_today = datetime.now().strftime('%d %B')
            msg_text = f"""
            {date_today} - Today's weather in {city}:
            Temperature: {weather_data['temp']}°C
            Description: {weather_data['description']}
            """
        else:
            msg_text = "Sorry, I couldn't fetch the weather data."
    else:
        msg_text = "Please set a city first using the command /weather <city_name>."

    bot.send_message(message.chat.id, msg_text)


@bot.message_handler(func=lambda message: message.text.lower() == 'tomorrow')
def get_weather_tomorrow(message):
    city = user_city.get(message.chat.id)
    if city:
        forecast_data = fetch_forecast(city, days=1)
        if forecast_data:
            bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            time.sleep(2)
            date_tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d %B')
            msg_text = f"""
            {date_tomorrow} - Tomorrow's weather in {city}:
            Temperature: {forecast_data['temp']}°C
            Description: {forecast_data['description']}
            """
        else:
            msg_text = "Error."
    else:
        msg_text = "Please set a city first using the command /weather <city_name>."

    bot.send_message(message.chat.id, msg_text)


@bot.message_handler(func=lambda message: message.text.lower() == '3 days')
def get_weather_3_days(message):
    city = user_city.get(message.chat.id)
    if city:
        forecast_data = fetch_forecast(city, days=3)
        if forecast_data:
            bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            time.sleep(2)
            msg_text = f"Weather for the next 3 days in {city}:\n{forecast_data}"
        else:
            msg_text = "Error."
    else:
        msg_text = "Please set a city first using the command /weather <city_name>."

    bot.send_message(message.chat.id, msg_text)


def fetch_weather(city):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather_info
    else:
        return None


def fetch_forecast(city, days):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(FORECAST_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if days == 1:
            forecast_info = data['list'][8]
            weather_info = {
                'temp': forecast_info['main']['temp'],
                'description': forecast_info['weather'][0]['description']
            }
        elif days == 3:
            forecast_list = data['list'][8:8 * 4:8]
            weather_info = "\n".join(
                [(datetime.now() + timedelta(days=i + 1)).strftime('%d %B') +
                 f" - Temp: {info['main']['temp']}°C, Description: {info['weather'][0]['description']}"
                 for i, info in enumerate(forecast_list[:3])]
            )
        return weather_info
    return None


@bot.callback_query_handler(func=lambda call: True)
def callback_button(call):
    if call.data == 'today':
        get_weather_today(call.message)
    elif call.data == 'tomorrow':
        get_weather_tomorrow(call.message)
    elif call.data == '3_days':
        get_weather_3_days(call.message)


bot.polling()
