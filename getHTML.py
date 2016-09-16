import requests
import time

def getHTML(daysago=-1):

    if daysago < 0:
        day = tday()
    else:
        day = tday()-daysago

    params = {
        "st": "2",
        "r": "4",
        "d": str(day),
        "D": "3180",
        "q": "текст",
    }

    try:
        r = requests.get("http://pikabu.ru/search.php", params=params)
    except:
        exit(322)

    print(r)
    r.url
    return r.text

def tday():
    now = time.time()
    then = time.mktime((2008, 1, 1, 0, 0, 0, 0, 0, 0))

    right = now - then
    days = int(right / 60 / 60 / 24)
    return days
