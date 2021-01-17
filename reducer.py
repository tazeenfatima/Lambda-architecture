#!/usr/bin/python

import sys

count_of_delayed_flights = 0
total_delayed_time = 0
prev_year = None
try:
  for line in sys.stdin:
    line = line.strip()
    #parse the input we got from mapper.py
    year, fl_delay = line.split('\t',1)
    #print year, fl_delay, type(fl_delay)
    # convert delay (currently a string) to float
    try:
      fl_delay = float(fl_delay)
    except ValueError:
      #delay was not a number, so silently ignore this line
      continue
    # this IF-switch only works because Hadoop sorts map output by key
    # (here: year) before it is passed to the reducer
    if prev_year == year:
      count_of_delayed_flights +=1
      total_delayed_time += fl_delay
    else:
      if prev_year:
        # write result to STDOUT
        print 'Average Delayed time in year %s is %s minutes' % (prev_year, total_delayed_time/count_of_delayed_flights)
      prev_year = year
      total_delayed_time = fl_delay
      count_of_delayed_flights = 1
  #last year output
  if prev_year == year:
    print 'Average Delayed time in year %s is %s minutes' % (year, total_delayed_time/count_of_delayed_flights)
except Exception as error:
  print 'Error occured at reducer', error
  pass

