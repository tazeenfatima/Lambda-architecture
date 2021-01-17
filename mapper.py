#!/usr/bin/python

import sys
import json

try:
  #input from text files exported from database
  data_arr = list()
  for line in sys.stdin:
    data_arr = data_arr + line.strip().split(';')
  for obj in data_arr:
    #print 'obj', obj
    json_obj = eval(obj)
    #all delayed flights which are not cancelled
    if json_obj['CANCELLED'] and json_obj['ARR_DELAY'] and int(float(json_obj['CANCELLED'])) == 0:
      fl_delay = float(json_obj['ARR_DELAY'])
      if fl_delay > 0:
        #write the results to standard output STDOUT
        print json_obj['FL_DATE'].split('-')[0], '\t', fl_delay
except Exception as error:
  print 'Error occured at mapper', error
  pass

