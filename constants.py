SCAN_TYPES = {
    1: "-sT -T4 -Pn --top-ports 100 --open --max-retries 1",
    2: "-sT -sV -T4 -Pn --top-ports 1024 --version-intensity 5 --open --max-retries 2 --host-timeout 60s",
    3: "-sT -sV -T3 -Pn --top-ports 10484 --version-intensity 7 --open --max-retries 3 --host-timeout 90s",
}














# SCAN_TYPES = {
#     # Fast discovery (no CVEs, just exposure check)
#     1: (
#         "-sT -T4 "
#         "--top-ports 100 "
#         "--open "
#         "--max-retries 1 "
#         "--script=banner"
#     ),

#     # Standard scan with service + CPE detection
#     2: (
#         "-sT -sV -T4 "
#         "--top-ports 1024 "
#         "--version-intensity 7 "
#         "--open "
#         "--max-retries 2 "
#         "--host-timeout 60s "
#         "--script=banner "
#         "--script-args=unsafe=1"
#     ),

#     # Full vulnerability scan (CVE-capable)
#     3: (
#         "-sT -sV -T3 "
#         "--top-ports 10484 "
#         "--version-intensity 9 "
#         "--open "
#         "--max-retries 3 "
#         "--host-timeout 90s "
#         "--script=vulners,vuln "
#         "--script-args=unsafe=1"
#     ),
# }
