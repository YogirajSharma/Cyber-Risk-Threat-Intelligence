## Layer 1: Discovery & Port Scanning
---
### For the attention of readers
>   This document explains how to set up, configure, and run **Layer 1: Discovery & Port Scanning**.
It is intended for developers who want to run the project locally, understand integrations, or extend intelligence sources.

## Pre — requesites
- OS (Windows / Linux Ubuntu)
- Python software, and pip installation manager [Install Python]()
- VS Code (Visual Studio Code) [Install VS Code]()
- Internet Connection
- Git

---

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

## Set up
1. Clone the repo, and get inside it
    ```
        Updated soon
    ```
2. [Virtual Environment Setup](CreateVirtualEnv.md)
3. Install all the libraries and packages inside the virtual environment. 
    ```bash
    > pip install -r requirements.txt
    ```
4. API setup<br>
    Updated Soon
5. Run the code:
    ```
        Updated soon

    ```
6. [Output Architecture: Updated Soon]()<br>
7. [Troubleshooting]()

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
