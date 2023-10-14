#!/usr/bin/env python

import sys

line = sys.stdin.readline()
# Skip first line. I'm sure there's an easier way to do this but I'm stumped
for line in iter(sys.stdin.readline, ''):
  while line:
    #Do something with line here to create/output
    #as many (key,value) pairs as you want.
    #Do not add anything above this line. The one 
    #exception is that you can add import statements.
          
    #Do not add anything below this line.
    #Read in the next line of the input.
        
    # Assign column names to make it easier to keep track of
    salesRecords = line.split(',')
    InvoiceNo = str(salesRecords[0])
    Quantity = float(salesRecords[3])
    InvoiceDate = str(salesRecords[4])
    UnitPrice = float(salesRecords[5])
    CustomerID = str(salesRecords[6])
    Country = str(salesRecords[7])
        
    # find the total spent in row
    totalSpent = Quantity * UnitPrice
        
    # Pull month from the date column
    InvoiceDate = InvoiceDate.split('/')
    InvoiceMonth = InvoiceDate[0]
        
    # Add 0 to beginning of month to fit directions
    if len(InvoiceMonth) == 1:
      InvoiceMonth = '0' + InvoiceMonth
        
    # Filter out rows that are returns
    if InvoiceNo[0] != 'c' and CustomerID != '':
      # I don't understand why but there seems to be a newline character at the end of country,
      # so .strip() was used to remove this. totalSpent had to be converted to a string to make Python happy.
      print('{0},{1}:{2} \t {3}'.format(InvoiceMonth, Country.strip(), CustomerID, str(totalSpent)))
    line = sys.stdin.readline()