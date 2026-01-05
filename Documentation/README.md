---

## Layer 1: Discovery & Port Scanning

### High-Level Overview

Layer 1 is responsible for initial reconnaissance and data collection. Its primary objectives include:

- Accepting scan targets such as:
  - Single IP address  
  - CIDR block  
  - IP range  
  - Domain name  
- Performing network discovery using **Nmap**
- Identifying:
  - Live hosts
  - Open ports
  - Running services and service versions
- Enriching discovered services with known vulnerability data (CVE) using:
  - NVD (National Vulnerability Database)
  - Vulnerability intelligence APIs (e.g., Vulners)
- Storing scan results in a **structured JSON format**

The output of this layer is consumed by later components for:
- Risk scoring
- Threat correlation
- Reporting and dashboards

---

## Layer 1 Structure (temporary)
```
project_root/
│
├── main.py
├── constants.py
├── config.py
│
├── scanner/
│   ├── nmap_scanner.py
│   ├── target_detection.py
│   └── result_formatter.py
│
├── cve/
│   └── nvd_client.py
│
├── utils/
│   └── logger.py
│
└── results/
    └── scan_YYYYMMDD_HHMMSS.json
```

---

## Execution Flow

1. **Target Input**
   - The user provides a scan target (IP, CIDR, range, or domain).

2. **Target Validation & Detection**
   - `target_detection.py` validates and normalizes the target format.

3. **Network Scanning**
   - `nmap_scanner.py` performs host discovery and port scanning.
   - Open ports, services, and versions are identified.

4. **Vulnerability Enrichment**
   - Service and version data are sent to the CVE module.
   - `nvd_client.py` retrieves related CVE information from vulnerability databases.

5. **Result Formatting**
   - `result_formatter.py` structures the data into a consistent JSON schema.

6. **Result Storage**
   - Scan results are saved in the `results/` directory with a timestamped filename.

---

## Module Documentation
This documantation is updated after all part will be completed

---
