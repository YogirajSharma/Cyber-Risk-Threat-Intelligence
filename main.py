import json
from datetime import datetime
from config import RESULTS_DIR
from scanner.nmap_scanner import NmapScanner
from scanner.result_formatter import format_results

def main():
    target = input("Target (IP / CIDR / Range / Domain): ").strip()
    scan_level = int(input("Scan Type (1=Quick, 2=Medium, 3=Deep): "))

    scanner = NmapScanner()
    nm, nm_args = scanner.scan(target, scan_level)
    results = format_results(nm, target, nm_args)

    filename = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = RESULTS_DIR / filename

    with open(filepath, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[+] Scan completed. Results saved to {filepath}")

if __name__ == "__main__":
    main()
