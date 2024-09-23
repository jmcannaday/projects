# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Jon Cannaday
# 11/14/2023

import requests

# Global variable for weather API key
weatherapi = '46bf9bd76e465bac84162b168e06ee6d'


# Coordinates are generated from the zip code option.
def zipcoordinates():
    usercountry = input('Country: (EX: US) ').lower()
    userzip = input('Zip Code: (EX: 75034) ')
    userzipapi = f"http://api.openweathermap.org/geo/1.0/zip?zip={userzip},{usercountry}&appid={weatherapi}"
    zipresponse = requests.get(userzipapi)
    zipdata = zipresponse.json()
    try:
        return zipdata['lat'], zipdata['lon']
    except (IndexError, KeyError):
        print('==================================')
        print('Invalid Location.')
        print('==================================')
        return None, None


# Coordinates are generated from the city state option.
def citycoordinates():
    usercountry = input('Country: (EX: US) ').lower()
    usercity = input('City: (EX: Frisco) ').lower()
    userstate = input('State: (EX: TX) ').lower()
    usercityapi = f"http://api.openweathermap.org/geo/1.0/direct?q={usercity},{userstate},{usercountry}&limit=1&appid={weatherapi}"
    cityrequest = requests.get(usercityapi)
    citydata = cityrequest.json()
    try:
        return citydata[0]['lat'], citydata[0]['lon']
    except (IndexError, KeyError):
        print('==================================')
        print('Invalid Location.')
        print('==================================')
        return None, None


# The coordinates are passed through this function to get the temperature.
def temperature(latitude, longitude):
    usermetric = input('Choose the temperature units. metric, imperial, or kelvin. If unkown Kelvin will be the default. ')
    temperatureapi = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weatherapi}&units={usermetric}"
    temperatureresponse = requests.get(temperatureapi)
    if temperatureresponse.status_code == 200:
        temperaturedata = temperatureresponse.json()
        print('================================================')
        print('Location: ', temperaturedata['name'])
        print('Temperature:    ', temperaturedata['main']['temp'], '  Feels like:      ',
              temperaturedata['main']['feels_like'])
        print('Min Temperature:', temperaturedata['main']['temp_min'], '  Max Temperature: ',
              temperaturedata['main']['temp_max'])
        print('Pressure:       ', temperaturedata['main']['pressure'], '    Humidity:        ',
              temperaturedata['main']['humidity'])
        print('Weather:        ', temperaturedata['weather'][0]['main'], '  Description:     ',
              temperaturedata['weather'][0]['description'])
        print('Wind Speed:     ', temperaturedata['wind']['speed'], '    Temperature(k):  ',
              temperaturedata['main']['temp'], 'K')
        print('================================================')
    else:
        print('Failed to retrieve temperature data.')


def userpathone():
    latitude, longitude = citycoordinates()
    if latitude is not None and longitude is not None:
        temperature(latitude, longitude)


def userpathtwo():
    latitude, longitude = zipcoordinates()
    if latitude is not None and longitude is not None:
        temperature(latitude, longitude)


def main():
    while True:
        print('Weather lookup options.')
        print('Enter 1 for City and State')
        print('Enter 2 for Zip Code')
        print('Enter 3 to Exit')
        userpath = input('Enter your choice: ')
        if userpath == '1':
            userpathone()
        elif userpath == '2':
            userpathtwo()
        elif userpath == '3':
            print('Program Closed.')
            break
        else:
            print('==================================')
            print('Invalid Entry.')
            print('==================================')


if __name__ == '__main__':
    main()
