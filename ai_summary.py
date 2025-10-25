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


    print("\n" + "="*50)
    print("🎯 **Project Log Analysis: Synchronization Summary** 📊")
    print("="*50)
    print(f"Total Sync Operations Recorded: {total_sync_runs}")
    print("-" * 35)
    print(f"| **File Operations:**")
    print("-" * 35)
    print(f"| Newly Copied Files:  {totals.get('Copied', 0):>15}")
    print(f"| Existing Files Updated: {totals.get('Updated', 0):>15}")
    print(f"| Files Skipped (No Change): {totals.get('Skipped', 0):>15}")
    print("-" * 35)

    error_count = totals.get('Errors', 0)
    if error_count > 0:
        print(f"| **Errors Encountered:** **{error_count}** :exclamation:")
        print("-" * 35)
    else:
        print(f"| Errors Encountered: {error_count:>15}")
        print("-" * 35)

    print("\nAnalysis complete. Consult the full log for detailed transactional records.")
    print("="*50)

if __name__ == "__main__":
    analyze_sync_report()
