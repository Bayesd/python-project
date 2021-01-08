import os
from datetime import date


def get_calendar():
    input = os.popen("cal")
    calendar = input.read()
    rows = calendar.splitlines()
    new_cal =""
    counter = 0
    todays_date = int(str(date.today())[-2:])
    for row in rows:
        row_str = str(rows[counter])
        new_cal += row_str + "\n"
        counter += 1
    top_cal = new_cal[:45]
    date_cal = new_cal[44:]
    date_cal = date_cal.replace(str(todays_date - 1), f"{str(todays_date - 1)} (")
    date_cal = date_cal.replace(str(todays_date + 1), f") {str(todays_date + 1)}")
    final_calendar = top_cal + date_cal
    return final_calendar

def append_file():
    file = open("/home/ubuntu/workspace/systemd_calendar.txt", "a+")
    file.write(get_calendar())

append_file()
