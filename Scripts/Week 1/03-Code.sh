#!/bin/bash
# Sierra Maldonado - worked with Justin H, Geneva & Nick A
https://subscription.packtpub.com/book/networking-and-servers/9781785286216/1/ch01lvl1sec17/working-with-permissions
https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/

#!/bin/bash
# Sierra Maldonado - worked with Justin H, Genvea & Nick A
# File permissions


#Prompt user for Doc
read -p "Type in the directory path you would like to edit permissions on?" Directory

#Prompt user for Command code
read -p "Type the command code to change the permissons" Code

# Check File permissions
ls -l "$Directory"

# Change file permissions
chmod -R "$Code" "$Directory"

echo "Permissions for directory and its contents have been updated successfully"


# end