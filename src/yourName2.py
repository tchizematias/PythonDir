#!/usr/bin/python

# There is a logic bug on this script which I haven't managed to understand yet
# the bug happens while executing " name = input() "
while True:
   print('Please type your name.')
   name = input()
   if name == 'your name':
      break
print('Thank you!')
