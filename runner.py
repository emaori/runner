
#!/usr/bin/python

import json
import time
import calendar
import subprocess
import sys
import platform
from datetime import datetime, time

def getTimeTuple(timeStr):
    return int(timeStr.split('.')[0]), int(timeStr.split('.')[1])

def exeTasks(tasks):
    for t in tasks:
        print(">>>>>>>>>> Going to launch "+ t)
        process = subprocess.Popen(t, stdout=subprocess.PIPE)

def exeSchedule(schedule):
    # Check the day
    #currentWeekDay = time.strftime("%A")
    if "name" in schedule:
        print(">>>>>> " + schedule["name"])

    # Check the platform
    if "platforms" in schedule:
        currentPlatform = platform.system()
        # If currentPlatform is an empty string it means that it cannot be determinated -> continue
        if not currentPlatform == "":
            if not currentPlatform in schedule["platforms"]:
                # This schedule cannot run in the current platform
                print("Current platform not supported by this schedule")
                return

    currentWeekDay = calendar.day_name[datetime.today().weekday()]
    if currentWeekDay in schedule["days"]:
        # Chck time
        startTimeTuple = getTimeTuple(schedule["startTime"])
        endTimeTuple = getTimeTuple(schedule["endTime"])
        if time(startTimeTuple[0], startTimeTuple[1]) <= datetime.now().time() <= time(endTimeTuple[0], endTimeTuple[1]):
            # If those match, execute the tasks
            exeTasks(schedule["tasks"])

# Take the path of the json file from first argument
# If there is no argument, just use the default (runner.json) file name and
# the current working directory
jsonFilePath = "runner.json"
if len(sys.argv) > 1:
    jsonFilePath = sys.argv[1]

# Read the json file
with open(jsonFilePath) as data_file:
    data = json.load(data_file)

if "enable" in data:
    if not data["enable"]:
        print("Exit without executing json file: it's disabled")
        sys.exit(0)

if "name" in data:
    print(">>> " + data["name"])
else:
    print(">>> Going to execute the json: " + jsonFilePath)

schedules = data["schedules"]

for s in schedules:
    # If enable field is not present, execute the schedule (so, default value is true)
    if "enable" in s:
        if not s["enable"]:
            continue
    exeSchedule(s)

print("Runner completed :)")