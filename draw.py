import requests
from io import BytesIO


def draw(ll, spn, mode='map'):
    map_params = {
        "ll": ",".join(map(str, ll)),
        "spn": ",".join(map(str, spn)),
        "l": mode}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        pass
    return BytesIO(response.content)