import requests
from io import BytesIO


def draw(ll, spn, pt=[], mode='map', size="100,100"):
    map_params = {
        "ll": ",".join(map(str, ll)),
        "spn": ",".join(map(str, spn)),
        "l": mode,
        "size": size,
        "pt": pt
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        pass
    return BytesIO(response.content)