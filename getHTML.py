import requests

def getHTML():
    params = {
        "n": "2",
        "st": "2",
        "r": "5",
        "d": "3135",
        "D": "3137",
        "q": "текст",
    }

    try:
        r = requests.get("http://pikabu.ru/search.php", params=params)
    except:
        exit()

    print(r)
    return r.text
