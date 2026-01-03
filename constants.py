SCAN_TYPES = {
    1: "-sT -T4 --top-ports 100 --open --max-retries 1",
    2: "-sT -sV -T4 --top-ports 1024 --version-intensity 5 --open --max-retries 2 --host-timeout 60s",
    3: "-sT -sV -T3 --top-ports 10484 --version-intensity 7 --open --max-retries 3 --host-timeout 90s",
}
