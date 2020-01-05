#!/usr/bin/env python

#Menu
print("""
   @@@@@@@@      @@@@@@@@@      @@@@@@@@@@     @@@@@@@@@@     @         @
   @             @              @        @     @        @     @         @
   @             @              @        @     @        @     @         @
   @             @              @        @     @       @      @         @
   @@@@@@@@      @@@@@@@@@      @@@@@@@@@@     @@@@@@@@       @@@@@@@@@@@
	  @      @              @        @     @       @      @         @
 	  @      @              @        @     @        @     @         @
	  @      @              @        @     @        @     @         @
   @@@@@@@@      @@@@@@@@@      @        @     @        @     @         @
""");

print("___________________________________________________________________________");
print("")
print("")
print("")

#Function	      
try:
	from googlesearch import search 
except ImportError:
	print("No module named 'google' found")

#How to Search

query = raw_input("What do you want to search for? ")

for j in search(query, tld="co.in", num = 20, stop = 20, pause = 2):
	print(j)

print("")
print("")
print("")

raw_input("Press ENTER to exit");




