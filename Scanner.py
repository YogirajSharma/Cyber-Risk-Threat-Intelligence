import nmap # Python wrapper for the Nmap tool
from ip_verification import detect_target_type
from show_result import generate_output

scanner = nmap.PortScanner() # Initializes Nmap scanner object

def scan_target(target: str):
    target_type = detect_target_type(target)
    print(f"[+] Target Type Detected: {target_type}")

    if target_type not in ["IP", "CIDR", "range", "domain"]:
        print("[-] Invalid target. Scan aborted.")
        return None

    nmap_arguments = "-Pn -p 1-1024 -T4 --max-retries 2 --host-timeout 30s"
    print(f"[*] Starting scan for {target}")

    try:
        scanner.scan(hosts=target, arguments=nmap_arguments) # Executes Nmap scan
        return generate_output(scanner, target) # Formats output

    except nmap.PortScannerError as e: # Handles Nmap-specific errors
        print(f"[-] Nmap Scan Error: {e}")
    except Exception as e: # Catches unexpected issues
        print(f"[-] Unexpected Error: {e}")

    return None
