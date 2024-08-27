import subprocess

def ping_without_ssh(source_ip, dest_ip):
    print(f"Pinging from {source_ip} to {dest_ip}...")
    response = subprocess.run(['ping', '-n', '4', dest_ip], stdout=subprocess.PIPE, text=True)
    print(response.stdout)

ping_without_ssh("192.168.0.1", "100.0.0.2")
#import paramiko

# Define the interface IPs and OAM IPs for the routers

# Define function to ping using Paramiko
# def ping_router(source_ip, dest_ip):
#     print(f"Pinging from {source_ip} to {dest_ip}...")

#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#     try:
#         # Connect to the source router
#         ssh.connect(hostname=source_ip, username='Sridevi_5thflr_2.4G', password='9686262574T', timeout=10)
#         # Execute the ping command
#         stdin, stdout, stderr = ssh.exec_command(f"ping -n 4 {dest_ip}")
#         output = stdout.read().decode()
#         error = stderr.read().decode()

#         # Print the output of the ping command
#         if output:
#             print(output)
#         if error:
#             print(f"Error: {error}")
#     except Exception as e:
#         print(f"Failed to ping from {source_ip} to {dest_ip}: {e}")
#     finally:
#         ssh.close()
# ping_router("192.168.0.1", "100.0.0.1")

