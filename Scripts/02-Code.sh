
#!/bin/bash
# Sierra Maldonado - worked with Justin H, Genvea & Nick A
# Import Datetime
# Used Shell gudie and display date links in the Resources
# Used ChatGBT to name the file todays date
# https://www.cyberciti.biz/faq/linux-log-files-location-and-how-do-i-view-logs-files/


#Varibles

source_path="/var/log/syslog"
dest_path=$(pwd)

# Set filename to todays date
filename=$(date +"%Y-%m-%d")

#copy
cp "$source_path" "$dest_path/$filename"
