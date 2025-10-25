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

    totals = defaultdict(int)
    total_sync_runs = 0

    for line in log_entries:
        if "New:" in line and "|" in line:
            total_sync_runs += 1
            try:
                summary_data = line.split("|", 1)[1]
                parts = summary_data.split(",")
                totals["Copied"] += int(parts[0].split(":")[1])
                totals["Updated"] += int(parts[1].split(":")[1])
                totals["Skipped"] += int(parts[2].split(":")[1])
                totals["Errors"] += int(parts[3].split(":")[1])

            except Exception as e:
                print(f"**Warning:** Could not parse a summary line due to format irregularity (ignoring entry). Details: {e}")
                continue

    if not totals and total_sync_runs == 0:
        print("\n**Report Analysis:** No completed synchronization run summaries were successfully parsed from the log.")
        return
