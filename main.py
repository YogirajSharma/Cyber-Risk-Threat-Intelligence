import json # Imports the built-in json module to format output as JSON.
from Scanner import scan_target # Imports the scan_target function from (Scanner.py).

def main():
    target = input("Enter IP / CIDR / range / domain: ").strip()
    output = scan_target(target)

    if output:
        print(json.dumps(output, indent=4)) # Converts Python dictionary → formatted JSON output.
    else:
        print("[-] No scan results returned.") # Handles empty or failed scans.
# Ensures the script only runs when executed directly (not imported)
if __name__ == "__main__":
    main()
