# Cyber Risk Assessment & Threat Intelligence Platform (Python)

## Project Overview

This project focuses on building a **Python-based Cyber Risk Assessment & Threat Intelligence Platform** that automates vulnerability discovery and enriches findings with threat intelligence. The platform is designed to help organizations understand their security posture, prioritize risks, and support compliance with security standards.

The system performs:
- Network discovery and vulnerability scanning  
- Risk-related data enrichment using threat intelligence sources  
- Structured reporting and visualization (in later layers)

This repository currently documents **Layer 1: Discovery & Port Scanning**, which serves as the foundation for subsequent risk analysis and threat intelligence layers.

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
______

## Setup and Run the Layer 1: 
[Click Here](Documentation/README.md) to see the developer documentation. 

---


## Summary

Layer 1 establishes the **discovery and data collection foundation** of the Cyber Risk Assessment & Threat Intelligence Platform. By combining network scanning with vulnerability intelligence and structured data storage, this layer enables:

- Accurate asset visibility  
- Early identification of security weaknesses  
- Reliable input for risk scoring and threat analysis in later layers  

Future layers will build upon this data to deliver risk assessment, threat correlation, alerting, dashboards, and compliance insights.

---
