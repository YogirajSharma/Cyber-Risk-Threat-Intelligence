from datetime import datetime, timezone
from cve.nvd_client import fetch_cve

def format_results(scanner, target: str, scan_command: str) -> dict:

    output = {
        "scan_time_utc": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3],
        "scanner_layer": "Discovery & Port Scanning",
        "target": target,
        "scan_command": scan_command,
        "total_hosts": 0,
        "total_open_ports": 0,
        "assets": [],
    }

    for host in scanner.all_hosts():
        asset = {
            "ip": host,
            "hostname": scanner[host].hostname(),
            "state": scanner[host].state(),
            "open_ports": []
        }

        for proto in scanner[host].all_protocols():
            for port, port_data in scanner[host][proto].items():
                if port_data.get("state") != "open":
                    continue

                product = port_data.get("product", "")
                version = port_data.get("version", "")

                port_entry = {
                    "port_no": port,
                    "protocol": proto,
                    "service": port_data.get("name", ""),
                    "product": product,
                    "version": version,
                    "cve": None
                }

                # Only attempt CVE lookup if a product was detected
                if product:
                    port_entry["cve"] = fetch_cve(product, version)

                asset["open_ports"].append(port_entry)
                output["total_open_ports"] += 1

        output["assets"].append(asset)
        output["total_hosts"] += 1

    return output
