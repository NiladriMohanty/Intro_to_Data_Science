'''
Author: Niladri
Last updated: 8 Jul 2015
Context: Returns Reformat Subway Dates
'''


import datetime
import time

def reformat_subway_dates(date):
    '''
    The dates in our subway data are formatted in the format month-day-year.
    The dates in our weather underground data are formatted year-month-day.
    
    In order to join these two data sets together, we'll want the dates formatted
    the same way.  Write a function that takes as its input a date in the MTA Subway
    data format, and returns a date in the weather underground format.
    
    Hint: 
    There are a couple of useful functions in the datetime library that will
    help on this assignment, called strptime and strftime. 
    More info can be seen here and further in the documentation section:
    http://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
    '''
    #d = date.split('-')
    #print d
    #d1 = [d[2],d[0],d[1]]
    #date_formatted = str(d1)# your code here
    
    temp = time.strptime(date, "%m-%d-%y")
    #print temp
    #print temp[0]
    #print temp[1]
    dt = datetime.datetime(temp[0], temp[1], temp[2])
    #print dt
    date_formatted = dt.strftime("%Y-%m-%d")# your code here
    return date_formatted
