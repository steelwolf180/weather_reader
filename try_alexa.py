import json
import request
from flask import Flask
from flask_ask import Ask, statement, question
from weather_forecast import get_24h_forecast 

app = Flask(__name__)
ask = Ask(app, '/weather_reader')

def get_weather():
    forecast = get_24h_forecast()

    forecast_msg = '{} with the lowest temperature at {} degrees celsius to highest {} degrees celsius. Humidity from lowest {} percent to highest {} percent.'.format(
        forecast['forecast'], forecast['temperature']['low'], forecast['temperature']['high'],
        forecast['relative_humidity']['low'], forecast['relative_humidity']['high'])
    return forecast_msg

@app.route('/')
def homepage():
    return 'Hi there, how your doing?'

@ask.launch
def start_skill():
    welcome_messsage = 'That\'s awesome!!!!! Would you like to know today\'s weather?'
    return question(welcome_messsage)

@ask.intent("YesIntent")
def share_weather():
    weather = get_weather()
    weather_msg = '"Currently, At PyCon APAC 2018 the forecast for today is {}"'.format(weather)
    return statement(weather_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Oh... that\'s too bad ... okay good bye then'
    return statement(bye_text) 

if __name__ == '__main__':
    welcome_messsage = 'Hello there, would you like the latest weather forcast?'
    app.run(debug=True)