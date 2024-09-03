import paramiko
import time
from getpass import getpass

host = "DESKTOP-DV4072N"
username = (input("Enter username:") or "admin")
password = getpass("Enter password:")

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(hostname=host,
                username=username,
                password=password)
stdin, stdout, stderr = session.exec_command('hostname')
time.sleep(.5)
print(f"Host Names is:{stdout.read().decode()}")
session.close()
