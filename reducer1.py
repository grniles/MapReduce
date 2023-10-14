#!/usr/bin/env python

import sys

# Set global variables
currentMonthCountry = None
currentMaxValue = 0
currentMaxCustomer = None
currentCustomer = None
currentValue = None

for line in sys.stdin:
  # strip lines and split on the tab to get month,country and id and value
  # split on : to get month and country and customerid
  line = line.strip()
  mcc, value = line.split('\t', 1)
  nextMonthCountry, nextCustomer = mcc.split(':',1)
  value = float(value)
  
  # Check if the country being looked as is equal to the next country.
  # Same for Customer. If yes, add the next value to overall value
  if currentMonthCountry == nextMonthCountry:
    if currentCustomer == nextCustomer:
      currentValue += value
    else:
      if currentCustomer:
        # If new customer value is greater than curent max value
        # Set currentvalue as maxvalue
        if currentValue >= currentMaxValue:
          currentMaxCustomer = currentCustomer
          currentMaxValue = currentValue
    currentValue = value
    currentCustomer = nextCustomer
  else:
    if currentMonthCountry:
      print('%s:%s' % (currentMonthCountry, currentMaxCustomer))
    currentMonthCountry = nextMonthCountry
    currentMaxCustomer = None
    currentMaxValue = 0
if currentMonthCountry == nextMonthCountry:
  print('%s:%s' % (currentMonthCountry, currentMaxCustomer))