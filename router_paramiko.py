import paramiko

# Define the routers and their IP addresses from the diagram
routers = {
    "Router A": ["100.0.0.1", "100.0.0.2"],
    "Router B": ["100.0.0.3", "100.0.0.4"],
    "Router X": ["20.0.0.5"],
    "Router Y": ["20.0.0.5"]
}

# Function to SSH into a router and execute the ping command
def ssh_and_ping(source_ip, destination_ip, router_ip):
    print(f"Connecting to {router_ip} and pinging from {source_ip} to {destination_ip}...")

    try:
        # Initialize SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the router (No username and password provided)
        client.connect(router_ip, username='your_username', password='your_password')
        
        # Execute the ping command
        stdin, stdout, stderr = client.exec_command(f'ping -n 4 {destination_ip}')
        
        # Print the output of the ping command
        print(stdout.read().decode())
        print(stderr.read().decode())
        
    finally:
        # Close the SSH connection
        client.close()

# SSH and ping from Router A to Router X and Y
for ip in routers["Router A"]:
    for dest_ip in routers["Router X"] + routers["Router Y"]:
        ssh_and_ping(ip, dest_ip, router_ip='10.0.0.5')

# SSH and ping from Router B to Router X and Y
for ip in routers["Router B"]:
    for dest_ip in routers["Router X"] + routers["Router Y"]:
        ssh_and_ping(ip, dest_ip, router_ip='10.0.0.6')