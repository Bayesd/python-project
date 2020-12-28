#! usr/bin/python3

import time
from threading import Timer
import requests


def get_time():
    t = time.localtime()
    current_time = time.strftime("%D", t)
    return(current_time)

"""
def timer():
    Timer(float(delay), timer).start()
    print("Hello")
"""

def append_file():
    file = open("namnsdagar.txt", "a+")
    file.write(get_todays_name_and_time())

def get_todays_name_and_time():
    r = requests.get("https://sholiday.faboul.se/dagar/v2.1/")
    my_dict = r.json()
    dict_in_dict = my_dict["dagar"][0]
    name = dict_in_dict["namnsdag"][0]
    time = my_dict["cachetid"]
    return f"{time}\nDagens namnsdag: {name}\n"

print(get_todays_name_and_time())
"""
delay = 24 * 60 * 60

timer()
"""
append_file()

