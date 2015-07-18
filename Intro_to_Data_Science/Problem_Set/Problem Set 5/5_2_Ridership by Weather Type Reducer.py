'''
Author: Niladri
Last updated: 8 Jul 2015
Context: Returns Ridership by Weather Type Reducer
'''

import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''
   
    entries = 0.0
    avg = 0.0
    num  = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) !=2:
            continue
        this_key, count = data
        
        if old_key and old_key != this_key:
            avg = entries/num
            print "{0}\t{1}".format(old_key,avg)
            entries = 0
            num = 0
        old_key = this_key
        entries += float(count)
        num += 1
        
    if old_key != None:
        avg = entries/num
        print "{0}\t{1}".format(old_key, avg)
'''
    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        
        data = line.strip().split("\t")
        
        # throw out invalid data
        if len(data) != 2:
            continue
        
        # this_key ends up being data[0]
        # count ends up being data[1], total numer of hourly riders
        this_key, count = data
           
        # data comes to us sorted, did we switch to the next key
        # if I switched keys, print out the key and its average
        if old_key and old_key != this_key:
            # we've switched to a new key
            myAverage = riders/num_hours
            print "{0}\t{1}".format(old_key, myAverage)
            # reset our counters
            riders = 0
            num_hours = 0

        old_key = this_key
        riders += float(count)
        num_hours += 1 
    
    # because there is no next key after the last key 
    # without this we would not include the last row
    if old_key != None:
        myAverage = riders/num_hours
        print "{0}\t{1}".format(old_key, myAverage)
'''
        
        
reducer()
