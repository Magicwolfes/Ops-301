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
butter= os.popen("ls").read()
taco= os.popen("whoami").read()
cheese= os.popen("lshw -short").read()

# Execute bash commands
print (butter, taco, cheese)

#Use print 3x
print ("this is my last print")

#end
