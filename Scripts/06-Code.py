#!/user/bin/env python3
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
# Python
#20Mar23
# https://www.geeksforgeeks.org/os-module-python-examples/


# main


#print the current working directory
print("Current working directory")

#Import os module
import os

# Define Var
butter= os.system("ls")
taco= os.system("whoami")
cheese= os.system("lshw -short")

# Execute bash commands
print (butter, taco, cheese)

#Use print 3x
print ("this is my last print")

#end