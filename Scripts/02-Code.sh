
#!/bin/bash
# Sierra Maldonado - worked with Justin H, Genvea & Nick A
# Import Datetime
# Used Shell gudie and display date links in the Resources


# Ask what document you want to add date"
read -p "What document would you like to add today's date to?" document

# Get todays date Y-M-D
date > document


echo "the date has been added"
