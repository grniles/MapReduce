#!/usr/bin/env python
 
 '''NOTE: I can't figure this one out. I feel like I'm close but I don't know what I'm missing'''
 
import sys
 
#Variables that keep track of the keys.
current_key_being_processed = None
maybeList = []
probablyList = []
currentValue = []

#Do not add anything above this line. The one
#exception is that you can add import statements.

#You can create any global variables you want here that you will use per key.
#For example, we can create a dictionary variable called temp and/or set a variable to 0:
#temp = {}
#temp_num = 0
#However, we must reset these once a new key is found, see below.

for line in sys.stdin:
  line = line.strip()
  next_key_found, value = line.split('\t', 1)
  next_key_found.strip()
  value = eval(value)
  value = [int(float(i)) for i in value]
  currentUser, relatedUser = next_key_found.split(' ')
  
  if current_key_being_processed == next_key_found:
    mutuals = [i for i in value if i in currentValue]
    print(mutuals)
    if len(mutuals) == 2 or len(mutuals) == 3:
      maybeList.extend(mutuals)
    if len(mutuals) >= 4:
      probablyList.extend(mutuals)
    print(maybeList)
    print(probablyList)
    #print(mutuals)
    #The next key read in is the same one we've been processing. 
    #You'll likely want to add some code here.

  else:
    #One of two things happened here:
    #1. The first key was found.
    #2. A new key was found.

    if current_key_being_processed:
      currentValue = value
      if len(maybeList) > 0 and len(probablyList) == 0:
        print('%s:Might%s' % (relatedUser, tuple(maybeList)))
      elif len(maybeList) == 0 and len(probablyList) > 0:
        print('%s:Probably%s' % (currentUser, tuple(probablyList)))
      elif len(maybeList) > 0 and len(probablyList) > 0:
        print('%s:Might%s Probably%s' % (currentUser, tuple(maybeList), tuple(probablyList)))
      else:
        print(currentUser + ':')
      #print('%s:Might(%s) Probably(%s)' % (next_key_found, [i.split(',') for i in maybeList], [i.split(',') for i in probablyList]))
      #2. happened, a new key was found.
      #Output something based on the (key,value) pairs that 
      #we have just seen where all of them had the same key.

      #end of the if statement for number 2. happening.
      
    #Since the next key found was a new key, we need to clear any global variables 
    #we have created right now. If we do not clear them out, our code is not stateless.
    #Therefore, we clear the dictionary and reset the variable to 0.
    #temp = {}
    #temp_num = 0
      
    #Lastly, we set the current_key_being_processed to be the new key we just read in.
    current_key_being_processed = next_key_found
    maybeList = []
    probablyList = []
  #for loop ends here

if current_key_being_processed == next_key_found:
    #Add any code you want here to take care of the last key that was processed.
    #print('%s:%s %s' % (personID, might, probably)
    print('%s:Might(%s) Probably(%s)' % (next_key_found, [i.split(',') for i in maybeList], [i.split(',') for i in probablyList]))