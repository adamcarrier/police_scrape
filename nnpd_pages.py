#!/usr/bin/env python3

# Get Daily Offense Reports pages in a dict
def get_offense_pages():
    offenses = {
        "Sunday": 'https://www2.nngov.com/newport-news/offenses/suntxt.htm',
        "Monday": 'https://www2.nngov.com/newport-news/offenses/montxt.htm',
        "Tuesday": 'https://www2.nngov.com/newport-news/offenses/tuetxt.htm',
        "Wednesday": 'https://www2.nngov.com/newport-news/offenses/wedtxt.htm',
        "Thursday": 'https://www2.nngov.com/newport-news/offenses/thutxt.htm',
        "Friday": 'https://www2.nngov.com/newport-news/offenses/fritxt.htm',
        "Saturday": 'https://www2.nngov.com/newport-news/offenses/sattxt.htm',
    }
    return offenses

# Get Daily Arrest Reports pages in a dict
def get_arrest_pages():
    arrests = {
        "Sunday": 'https://www2.nngov.com/newport-news/arrests/suntxt.htm',
        "Monday": 'https://www2.nngov.com/newport-news/arrests/montxt.htm',
        "Tuesday": 'https://www2.nngov.com/newport-news/arrests/tuetxt.htm',
        "Wednesday": 'https://www2.nngov.com/newport-news/arrests/wedtxt.htm',
        "Thursday": 'https://www2.nngov.com/newport-news/arrests/thutxt.htm',
        "Friday": 'https://www2.nngov.com/newport-news/arrests/fritxt.htm',
        "Saturday": 'https://www2.nngov.com/newport-news/arrests/sattxt.htm'
    }
    return arrests