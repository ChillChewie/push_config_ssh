import paramiko
import time
import os
from getpass import getpass
from hosts import network_devices
from configs import commands


user = input("Username : ")
pwd = getpass()

# For loop allows you to specify number of hosts
for ip in  network_devices:
    print(ip)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=user, password=str(pwd))
    connection = ssh.invoke_shell()
    connection.send('term len 0\n')
    time.sleep(1)
    for command in commands:
        connection.send(' %s \n' % command)
        time.sleep(2)
        buf = connection.recv(65000)
        f = open('logfile.txt', 'a')
        f.write(str(buf))
        f.close()
    print('done')
    ssh.close()
