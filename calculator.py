# imports
import requests # import the requests module
import json # import the json module
import sys # import the sys module

url_link = 'url' # url of the sourcebin
response = requests.get(url_link) # get the data from the url

if response.status_code == 200: # if the response is good
    
    data = response.text # get the data from the url

    data = data.split() # split the data into an array

    total_time = 0 # store the ms in this array
    for i in data: # loop through the array
        if 'ms' in i: # if ms is in the array
            i = int(i.replace('ms', '')) # remove the ms from the string
            total_time += i # add the ms to the total_time

    days = total_time // (24 * 3600 * 1000) # calculate the days
    total_time = total_time % (24 * 3600 * 1000) # calculate the remaining time
    hours = total_time // (3600 * 1000) # calculate the hours
    total_time %= (3600 * 1000) # calculate the remaining time
    minutes = total_time // (60 * 1000) # calculate the minutes
    total_time %= (60 * 1000) # calculate the remaining time
    seconds = total_time // 1000 # calculate the seconds

    print(f'Total Time Logged: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds') # print the total time