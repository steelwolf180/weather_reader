import requests

def get_2h_forecast(area):
    r = requests.get('https://api.data.gov.sg/v1/environment/2-hour-weather-forecast')
    data = r.json()
    items = data['items']
    forecasts = {}

    for i in items:
        for j in i['forecasts']:
            forecasts[j['area']] = j['forecast']
    
    return forecasts[area]

def get_24h_forecast():
    r = requests.get('https://api.data.gov.sg/v1/environment/24-hour-weather-forecast')
    data = r.json()
    general = data['items'][0]['general']

    return general
