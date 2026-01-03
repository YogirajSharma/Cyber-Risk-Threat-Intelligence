import ipaddress
import re

def detect_target_type(target: str) -> str:
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

    if re.fullmatch(r"(\d{1,3}\.){3}\d{1,3}-\d{1,3}", target):
        return "RANGE"

    if re.fullmatch(r"(?!-)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}", target):
        return "DOMAIN"

    return "INVALID"
