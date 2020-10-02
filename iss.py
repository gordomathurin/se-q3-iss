#!/usr/bin/env python

__author__ = 'Gordon'

import requests
import turtle

# astro_response = requests.get('http://api.open-notify.org/astros.json')
# space_station_response = requests.get(
#     'http://api.open-notify.org/iss-now.json')

# astro_json = astro_response.json()
# space_station_json = space_station_response.json()

# # name_access = astro_json['people']
# # for full_name in name_access:
# #     print(f"{full_name['name']} is on the {full_name['craft']} spacecraft")
# # print(f"Total number of people on space station: {astro_json['number']}")


# print(space_station_json)
# position_access = space_station_json['iss_position']
# for coords in position_access:
#     print(
#         f"Longitude: {position_access['longitude']} and Latitude: {position_access['latitude']}")


def get_coords():
    space_station_response = requests.get(
        'http://api.open-notify.org/iss-now.json').json()

    print(space_station_response)
    return(space_station_response)


def earth(iss_location):
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

    # always last line
    turtle.done()


def main():
    location_iss = get_coords()
    earth(location_iss)


if __name__ == '__main__':
    main()
