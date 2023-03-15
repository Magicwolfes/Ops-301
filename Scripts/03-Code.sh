#!/bin/bash
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
https://subscription.packtpub.com/book/networking-and-servers/9781785286216/1/ch01lvl1sec17/working-with-permissions
https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/

#!/bin/bash
# Sierra Maldonado - worked with Justin H, Genvea & Nick A
# File permissions


#Prompt user for Doc
read -p "Which Document would you like to edit permissions?" Document

#Prompt user for Command code
read -p "Type the command code to change the permissons" Code

# Check File permissions
ls -l "$Document"

# Change file permissions
chmod "$Code" "$Document"

echo "File permissions updated successfully"


# end