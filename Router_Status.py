import paramiko
import time
import sys
import os

# Predefined ip address to Open Gear
HOSTNAME = "152.94.73.138" # IP to Open Gear 1

response = os.system("ping " + HOSTNAME + ' -n ' + '1')

# Check response
if response == 0:
  print '\n\nConnection to Open Gear is up! Have fun!\n'
  time.sleep(2)
  print 'SSH is ready to establish connection to the Open Gear\n'
else:
  sys.exit("\n\nForce Ending Code - **ABORTING**\n"
           "\nConnection to the Open Gear is down! Please check the Open Gear and the physical connections!"
           "\n---------------------------------------------------------------------------------------------")