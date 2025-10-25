import os
from collections import defaultdict

def analyze_sync_report(report_filename="sync_log.txt"):    
    if not os.path.exists(report_filename):
        print(f"**Error:** Synchronization report file not found. Please ensure '{report_filename}' exists in the current directory.")
        return
