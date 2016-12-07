__author__ = 'Damien'

import paramiko
import time
import sys
import os

def open_gear_stat():
# Predefined ip address to Open Gear
    INDATA = raw_input('\nType a for Open Gear 1, b for Open Gear 2 or any other key to manually insert IP\n\n')

    if INDATA == 'a':
        print '\nOpen Gear 1 Selected'
        HOSTNAME = '152.94.73.138'
        # print "\n" + HOSTNAME
    elif INDATA == 'b':
        print 'Open Gear 2 Selected'
        HOSTNAME = '152.94.73.139'
        # print "\n" + HOSTNAME
    else:
        HOSTNAME = raw_input('Please type in a valid IP address to the Open Gear:\n\n')
        # print "\n" + HOSTNAME

    time.sleep(2)

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