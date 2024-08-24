import subprocess

# Define the IP addresses for the routers
routers = {
    "Router A": ["100.0.0.1", "100.0.0.2"],# Internal IPs of Router A
    "Router B": ["100.0.0.3", "100.0.0.4"],  # Internal IPs of Router B
    "Router C": ["20.0.0.5"],  # OAM IP of Router X (considered as Router C)
    "Router D": ["20.0.0.5"]   # OAM IP of Router Y (considered as Router D)
}

def ping_router(source, destination):
    print(f"Pinging from {source} to {destination}...")
    response = subprocess.run(['ping', '-n', '4', destination], stdout=subprocess.PIPE, text=True)
    print(response.stdout)

# Ping from Router A's interfaces to Router C and D
for ip in routers["Router A"]:
    for dest_ip in routers["Router C"] + routers["Router D"]:
        ping_router(ip, dest_ip)

# Ping from Router B's interfaces to Router C and D
for ip in routers["Router B"]:
    for dest_ip in routers["Router C"] + routers["Router D"]:
        ping_router(ip, dest_ip)
