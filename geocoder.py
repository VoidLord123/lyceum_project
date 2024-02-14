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


def get_object_coord(object_name):
    obj = get_info(object_name)
    if obj:
        return obj["Point"]['pos']
