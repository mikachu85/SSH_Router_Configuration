import paramiko
import time
import credentials

def router_settings_basic():
    PORT = 3033
    #PORT = int(input('Type in port number for the Router / Switch\n\n'))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Add policy (RSA Crypt key)
    print "\n\nSSHClient loaded..\n\n" + time.sleep(1) + "Policy Added..\n"
    ssh.connect('152.94.73.138', port=PORT, username=credentials.username, password=credentials.password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('\n')
    ssh_stdin.write('enable\nconf term\nno ip domain-lookup\n')
    time.sleep(0.5)
    ssh_stdin.write('line con 0\npassword cisco\nlogin\nlogging synchronous\nexit\n')
    time.sleep(0.4)
    ssh_stdin.write('line vty 0 4\npassword cisco\nlogin\nexit\nbanner motd #\nUnauthorized Access Prohibited #\nexit\nexit\n')
    time.sleep(0.2)
    print "\nBasic configuration uploaded successfully to unit"


# def router_settings_eigrp():
    # Warning ---Start from Conf Term---
    # print "SSHClient loaded..\n\nPolicy Added..\n"
    # ssh_stdin.write('router eigrp 1\nnetwork 10.1.1.0 0.0.0.255\n')
    # time.sleep(0.4)
    # ssh_stdin.write('eigrp log-neighbor-changes\nno auto-summary')

#
# def router_settings_ospf():
#
#
# def router_settings_vlan():

