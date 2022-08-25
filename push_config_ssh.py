import paramiko
import time
import os
import maskpass
from hosts import network_devices
from configs import commands


user = input("Username : ")
pwd = maskpass.advpass() 


# For loop allows you to specify number of hosts
for ip in  network_devices:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=user, password=pwd)
    remote = twrssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
    for command in commands:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        f = open('logfile.txt', 'a')
        f.write(str(buf))
        f.close()
    twrssh.close()

