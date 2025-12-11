import ipaddress
import re

def detect_target_type(target: str):
    """
    Detect whether the provided target is:
    - CIDR (e.g., 192.168.1.0/24)
    - Single IP (IPv4 or IPv6)
    - IP range (e.g., 192.168.1.10-20)
    - Domain (example.com)
    """

    target = target.strip()
    try:
        if "/" in target:
            ipaddress.ip_network(target, strict=False)
            return "CIDR"
    except ValueError:
        pass
    try:
        ipaddress.ip_address(target)
        return "IP"
    except ValueError:
        pass
    range_pattern = r"^(\d{1,3}\.){3}\d{1,3}-\d{1,3}$"
    if re.match(range_pattern, target):
        base_ip, range_end = target.split("-")
        try:
            ipaddress.ip_address(base_ip)
            last_octet = int(range_end)
            if 0 <= last_octet <= 255:
                return "range"
        except ValueError:
            pass
    domain_pattern = r"^(?!-)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    if re.match(domain_pattern, target):
        return "domain"
    return "Invalid target format"
