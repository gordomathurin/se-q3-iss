#!/usr/bin/env python

__author__ = 'Gordon Mathurin'

import requests
import turtle
import time


def get_astro_info():
    astro_response = requests.get('http://api.open-notify.org/astros.json')
    astro_json = astro_response.json()
    name_access = astro_json['people']
    print(
        f"Total number of people on space station: {astro_json['number']}")
    for full_name in name_access:
        print(f"{full_name['name']} is on the {full_name['craft']} spacecraft")


def get_space_station_info():
    space_station_response = requests.get(
        'http://api.open-notify.org/iss-now.json')
    space_station_json = space_station_response.json()
    # print(space_station_json)
    position_access = space_station_json['iss_position']
    for coords in position_access:
        print(f"Longitude: {position_access['longitude']}")
        print(f"Latitude: {position_access['latitude']}")


def indy_iss_over():
    params = {'lat': float(39.768402), 'lon': float(-86.158066)}
    r = requests.get('http://api.open-notify.org/iss-pass.json',
                     params=params).json()

    access_response = r['response'][0]['risetime']
    convert_time = time.ctime(access_response)
    print(convert_time)
    return convert_time


def get_coords():
    space_station_response = requests.get(
        'http://api.open-notify.org/iss-now.json').json()
    # print(space_station_response)
    return(space_station_response)


def map_drawing(iss_location):
    turtle_screen = turtle.Screen()
    turtle_screen.bgpic('map.gif')
    turtle.setup(width=720, height=360, startx=None, starty=None)
    turtle_screen.setworldcoordinates(-180, -90, 180, 90)
    turtle_screen.register_shape('iss.gif')

    # this part setup the ISS
    iss = turtle.Turtle()
    iss.shape('iss.gif')

    latitude = float(iss_location['iss_position']['latitude'])
    longitude = float(iss_location['iss_position']['longitude'])

    iss.penup()
    iss.goto(longitude, latitude)


def indy_mapping():
    # this part setup the ISS
    latitude = float(39.768402)
    longitude = float(-86.158066)
    indy_iss = turtle.Turtle()
    indy_iss.penup()
    indy_iss.goto(longitude, latitude)
    indy_iss.color('red')
    indy_iss.dot(8)
    indy_iss.write(indy_iss_over())
    indy_iss.hideturtle()
    turtle.done()


def main():
    get_astro_info()
    get_space_station_info()
    location_iss = get_coords()
    map_drawing(location_iss)
    indy_mapping()
    indy_iss_over()


if __name__ == '__main__':
    main()
