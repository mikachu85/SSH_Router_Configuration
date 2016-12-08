__author__ = 'Damien'

from Data import configuration
import Open_Gear_status
import credentials
import paramiko
import time
import sys


# Open Gear Status
Open_Gear_status.open_gear_stat()

# SSH Package
configuration.router_settings_basic()

# configuration.router_settings_vlan()

# configuration.router_settings_eigrp()

# configuration.router_settings_ospf()


