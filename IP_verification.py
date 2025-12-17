import ipaddress # Built-in module to validate IP addresses and networks.
import re # Used for regex pattern matching.

def detect_target_type(target: str) -> str:
    target = target.strip()

    # CIDR Detection
    try:
        if "/" in target:
            ipaddress.ip_network(target, strict=False) # Validates IPv4 or IPv6 address. strict=False allows non-network addresses.
            return "CIDR"
    except ValueError:
        pass

    # Single IP Detection
    try:
        ipaddress.ip_address(target)
        return "IP"
    except ValueError:
        pass

    # IP Range Detection(192.168.1.10-20)
    range_pattern = r"^(\d{1,3}\.){3}\d{1,3}-\d{1,3}$"
    if re.match(range_pattern, target):
        base_ip, last_octet = target.split("-")
        try:
            ipaddress.ip_address(base_ip)
            if 0 <= int(last_octet) <= 255:
                return "range"
        except ValueError:
            pass

    # Domain Detection
    domain_pattern = r"^(?!-)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    if re.match(domain_pattern, target):
        return "domain"

    return "invalid"
