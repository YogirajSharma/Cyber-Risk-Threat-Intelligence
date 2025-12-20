from datetime import datetime # Used for timestamps.

def generate_output(scanner, target):
    # Initializes final output structure
    output = {
        "scan_metadata": {
            "scan_id": f"scan-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            "scan_time": datetime.utcnow().isoformat() + "Z",
            "scanner_layer": "Discovery & Port Scanning",
            "tools_used": ["Nmap"],
            "scan_type": "unauthenticated",
            "target": target
        },
        "assets": [],
        "network_surface": {
            "total_hosts": 0,
            "total_open_ports": 0
        }
    }

    for host in scanner.all_hosts(): # scanner.all_hosts() returns a list of IP addresses.
        asset = {
            "ip": host, # Saves the host’s IP address.
            "hostname": scanner[host].hostname(), # Retrieves the DNS hostname (if available). 
            "state": scanner[host].state(), # Indicates whether the host is up, down, etc.
            "open_ports": [] # Prepares a list to store open ports for this host.
        }

        for proto in scanner[host].all_protocols(): # Iterates over protocols detected on the host.
            for port, port_data in scanner[host][proto].items(): # Iterates through each port under the given protocol.
                if port_data.get("state") == "open": #Only processes ports that are open. Ignores filtered or closed ports.
                    asset["open_ports"].append({ # Appends a dictionary describing the open port.
                        "port": port, # Stores the numeric port (e.g., 22, 443).
                        "protocol": proto, # Stores the protocol (tcp or udp).
                        "service": port_data.get("name"), # Service name detected by Nmap (e.g., http, ssh).
                        "product": port_data.get("product"), # Software running on the port (if detected). Example: Apache httpd
                        "version": port_data.get("version") # Version of the detected product (if available).
                    })
                    output["network_surface"]["total_open_ports"] += 1 # Updates the global count of open ports.

        output["assets"].append(asset) # Adds the completed host record to the assets list.
        output["network_surface"]["total_hosts"] += 1 # Tracks how many hosts were processed.

    return output # Returns the complete dictionary
