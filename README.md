# Runner

`Runner` is an easy peasy python script to run programs according to some conditions.
The current supported conditions are:
* day of week
* time (hh:mm)

Other conditions will be added in the future:
* platform (mac/linux/windows)
* enable/disable flag

## Contents
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)

## Installation


## Configuration
Edit `runner.json` and add the conditions and the programs to run. For instance, this is the configuration if you want to start notepad every day from 9am to 10pm:

```json
{
    "name" : "Name or description of the json file",
    "schedules" :[
        {
            "days" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "startTime" : "9.00",
            "endTime" : "22.00",
            "tasks" : [
                "notepad"
            ]
        }
    ]
}
```

## Usage
Execute the python script:

`python runner.py`

By default it takes a file named `runner.json` placed in the same folder of the script. If you want to use a different `.json` file:

`python runner.py alternativeRunner.json`

You can also configure your system to execute `runner.py` at the system start-up: that's actually the idea behind `runner.py`! :blush: