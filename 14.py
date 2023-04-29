import datetime
from time import sleep
import requests


#
# print(datetime.datetime.now())
# sleep(1)
# print(datetime.datetime.now())

def check_if_url_is_up(url):
    response = requests.get(url)
    if response.status_code < 300:
        return True
    else:
        return False


print(check_if_url_is_up("https://www.google.co.il/"))
