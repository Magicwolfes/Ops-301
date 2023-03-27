#!/usr/bin/env python3
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
# Import Directories 
# https://stackoverflow.com/questions/64455223/convert-a-for-loop-to-a-function-python-and-function-argument-clarification
# ChatGBT to understand how to do User inputs
# Main

import os

# Read user input
filename = input("Please enter the path to a directory: ")

# Get the absolute path of the chosen directory
root = os.path.abspath(filename)

# Get a list of subdirectories in the chosen directory
dirs = [os.path.join(filename, subdirectory) for subdirectory in os.listdir(filename) if os.path.isdir(os.path.join(filename, subdirectory))]

# Get a list of files in the chosen directory
files = [os.path.join(filename, file) for file in os.listdir(filename) if os.path.isfile(os.path.join(filename, file))]

#Array
array= (files, root, dirs)

# Function
def super(msg, com):
    print(msg + com)
    os.system(com)
    
# Loop through files and call the super function
for item in array:
    print(item)


#How i did it first

def chicken():
    for (root, dirs, files) in os.walk(filename):
        ### Add a print command here to print ==root==
        print(f'Root Directory:  + {root}')
        ### Add a print command here to print ==dirs==
        print(f'Subdirectory: {dirs}')
        ### Add a print command here to print ==files==
        print(f'Files: {files}')

chicken()

# end

