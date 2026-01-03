import nmap
from constants import SCAN_TYPES
from scanner.target_detection import detect_target_type
from utils.logger import get_logger

logger = get_logger("NmapScanner")

class NmapScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan(self, target: str, scan_level: int):
        target_type = detect_target_type(target)

        if target_type == "INVALID":
            raise ValueError("Invalid scan target")

        arguments = SCAN_TYPES.get(scan_level)
        if not arguments:
            raise ValueError("Invalid scan type selected")

        logger.info(f"Starting scan | Target={target} | Type={target_type}")
        self.scanner.scan(hosts=target, arguments=arguments)
        return self.scanner, arguments
