import requests

def getHTML():
    params = {
        "st": "2",
        "r": "6",
        "d": "3179",
        "D": "3180",
        "t": "текст"
    }
    r = requests.get("http://pikabu.ru/search.php", params=params)

    return r.text