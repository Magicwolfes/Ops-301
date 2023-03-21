#!/usr/bin/env python3
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
# Import Directories 
# https://stackoverflow.com/questions/64455223/convert-a-for-loop-to-a-function-python-and-function-argument-clarification
# ChatGBT to understand how to do User inputs
# Main

import os

### Read user input here into a variable

filename= input("please type your filepath")

# # Declaration of functions
def chicken():
    for (root, dirs, files) in os.walk(filename):
        ### Add a print command here to print ==root==
        print(f'Root Directory:  + {root}')
        ### Add a print command here to print ==dirs==
        print(f'Subdirectory: {dirs}')
        ### Add a print command here to print ==files==
        print(f'Files: {files}')

chicken()


# End
