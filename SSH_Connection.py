__author__ = 'Damien'

import paramiko
import time
import credentials
import sys

PORT = int(input('Type in port number for the Router / Switch\n\n'))
#PORT = 3033

# SSH Package
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Add policy (RSA Crypt key)

ssh.connect('152.94.73.138', port=PORT, username=credentials.username, password=credentials.password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('\n')
ssh_stdin.write('enable\nconf term\nno ip domain-lookup\n')
time.sleep(1)
ssh_stdin.write('banner motd #Unauthorized access denied#\nexit\n')
