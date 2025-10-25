import os
from collections import defaultdict

def analyze_sync_report(report_filename="sync_log.txt"):
    if not os.path.exists(report_filename):
        print(f"**Error:** Synchronization report file not found. Please ensure '{report_filename}' exists in the current directory.")
        return

    try:
        with open(report_filename, "r") as f:
            log_entries = [line.strip() for line in f if line.strip()]

    except IOError as e:
        print(f"**Critical Error:** Unable to read the report file '{report_filename}'. Details: {e}")
        return

    if not log_entries:
        print(f"**Report Analysis:** The synchronization log file ('{report_filename}') is present but contains no recorded entries.")
        return 
