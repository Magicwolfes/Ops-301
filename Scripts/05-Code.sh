#!/bin/bash
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
# Clear Log files
#17Mar23
# https://computingforgeeks.com/how-to-empty-truncate-log-files-in-linux/

#main

#prompt user for logfile
read -p "Type which log file you would like to clear" Logfile

#Clear log file 

:> $Logfile

#end
