#!/bin/python3
time = input().strip()
hour = time[:2]
body = time[2:8] 
xm   = time[8:]

if xm == "PM":
    if hour != "12":
        hour = "{0:02d}".format(int(hour) + 12)
elif hour == "12":
    hour = "00"
print(hour + body)
