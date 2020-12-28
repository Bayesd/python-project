import os
from datetime import date

input = os.popen("cal")
calendar = input.read()
rows = calendar.splitlines()

new_cal =""
counter = 0
todays_date = str(date.today())[-2:]
# Combining the rows back to a string
for row in rows:
    row_str = str(rows[counter])
    new_cal += row_str + "\n"
    counter += 1

dates = new_cal[44:].replace("28", f"({todays_date})")
print(dates)

final_cal = new_cal.replace("28", "fart")
print(final_cal)
print(todays_date)

