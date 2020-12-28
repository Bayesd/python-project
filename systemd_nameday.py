#!/usr/bin/python3.8

import requests

def append_file():
    file = open("/home/ubuntu/workspace/systemd_namnsdag.txt", "a+")
    file.write(get_todays_name_and_time())

def get_todays_name_and_time():
    r = requests.get("https://sholiday.faboul.se/dagar/v2.1/")
    my_dict = r.json()
    dict_in_dict = my_dict["dagar"][0]
    name = dict_in_dict["namnsdag"][0]
    time = my_dict["cachetid"]
    return f"{time}\nDagens namnsdag: {name}\n\n"

append_file()
