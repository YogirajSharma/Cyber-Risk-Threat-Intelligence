import requests
from functools import lru_cache
from config import NVD_API_URL, NVD_TIMEOUT, NVD_RESULTS_LIMIT

HEADERS = {"User-Agent": "Enterprise-Vuln-Scanner/1.0"}

@lru_cache(maxsize=256)
def fetch_cve(product: str, version: str | None = None):
    if not product:
        return {
            "cve": "N/A",
            "title": "No CVE data available",
            "cvss_score": None,
            "severity": "UNKNOWN"
        }

    params = {
        "keywordSearch": f"{product} {version or ''}".strip(),
        "resultsPerPage": NVD_RESULTS_LIMIT
    }

    try:
        response = requests.get(
            NVD_API_URL,
            headers=HEADERS,
            params=params,
            timeout=NVD_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()

        vulns = data.get("vulnerabilities", [])
        if not vulns:
            return {
            "cve": "N/A",
            "title": "No CVE data available",
            "cvss_score": None,
            "severity": "UNKNOWN"
        }

        cve = vulns[0]["cve"]
        metrics = cve.get("metrics", {})

        score = None
        if "cvssMetricV31" in metrics:
            score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
        
        if score is None:
            severity_type = "UNKNOWN"
        elif score >= 9.0:
            severity_type = "CRITICAL"
        elif score >= 7.0:
            severity_type = "HIGH"
        elif score >= 4.0:
            severity_type = "MEDIUM"
        else:
            severity_type = "LOW"

        return {
            "id": cve.get("id"),
            "description": cve["descriptions"][0]["value"],
            "cvss": score,
            "severity": severity_type
        }

    except Exception:
        return {
            "cve": "N/A",
            "title": "No CVE data available",
            "cvss_score": None,
            "severity": "UNKNOWN"
        }
