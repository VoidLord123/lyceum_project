import json
from pprint import pprint

import requests


def get_info(object_name):
    params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": object_name,
        "lang": "ru_RU",
        "format": "json"
    }
    response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=params)
    if not response:
        return None
    js = response.json()
    try:
        member = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        return member
    except Exception:
        return None
    return None


def get_object_coord(member):
    try:
        return member["Point"]["pos"].split()
    except KeyError:
        return ''


def get_object_address(member):
    try:
        return member["metaDataProperty"]['GeocoderMetaData']['Address']['formatted']
    except KeyError:
        return ''


def get_object_postcode(member):
    try:
        return member["metaDataProperty"]['GeocoderMetaData']['Address']['postal_code']
    except KeyError:
        return ''


def get_organisation_properties(address_ll):
    search_params = {
        "apikey": 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3',
        "lang": "ru_RU",
        "text": get_object_address(get_info(address_ll)),
        "type": 'biz',
        "ll": address_ll
    }
    search_api_server = "https://search-maps.yandex.ru/v1/"
    response = requests.get(search_api_server, params=search_params)
    if not response:
        pass
    json_response = response.json()["features"]
    organization = json_response[0]
    company_data = organization["properties"]["CompanyMetaData"]
    address = company_data["address"]
    coords = organization['geometry']['coordinates']
    return address, coords