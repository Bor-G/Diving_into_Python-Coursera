import requests
import pprint

def get_location_info():
    return requests.get("http://api.ipstack.com/134.249.189.127?access_key=bc89a2b366ec364ba63923fc27f873c9").json()


if __name__ == "__main__":
    pprint.pprint(get_location_info())