#!/bin/bash
# Sierra Maldonado - worked with Justin H, Genvea & Nick A
# Conditionals


#main
#Loop

while true; do
    clear
    #Choices
    echo "1) hello world"
    echo "2) ping" 
    echo "3) ip info"
    echo "4) exit"

    #User input
    read -p "Please select one of the above options" Choice

    #choice options
    case $Choice in
        1)
            echo "hello world"
            read -p "Enter to continue"
            ;;
        2) 
            ping -c 4 192.168.0.208
            read -p "Enter to continue"
            ;;
        3)
            ip a 
            read -p "Enter to continue"
            ;;
        4)
            exit 0
            ;;
    esac
done

