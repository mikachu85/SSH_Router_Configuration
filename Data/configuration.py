import paramiko
import time

ssh = paramiko.SSHClient()
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('\n')

def router_settings_basic():
    ssh_stdin.write('enable\nconf term\nno ip domain-lookup\n')
    time.sleep(1)
    ssh_stdin.write('banner motd #Unauthorized access denied#\nexit\n')
    time.sleep(1)
    ssh_stdin.write('conf term\nline con 0\nloggin sync\npassword cisco\nlogin\nexit\n')
    time.sleep(1)
    ssh_stdin.write('line vty 0 4\npassword cisco\nexit\n')
    time.sleep(1)