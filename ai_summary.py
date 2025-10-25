import os

def summarize_logs(log_file="sync_log.txt"):
    if not os.path.exists(log_file):
        print("No log file found.")
        return

    with open(log_file, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        print("Log file is empty.")
        return

    copied, updated, skipped, errors = 0, 0, 0, 0
    for line in lines:
        if "New:" in line:
            try:
                parts = line.split("|")[1].split(",")
                copied += int(parts[0].split(":")[1])
                updated += int(parts[1].split(":")[1])
                skipped += int(parts[2].split(":")[1])
                errors += int(parts[3].split(":")[1])
            except:
                continue

    print("\n--- Sync Activity Summary ---\n")
    print(f"Total Sync Operations: {len(lines)}")
    print(f"Files Copied: {copied}")
    print(f"Files Updated: {updated}")
    print(f"Skipped Files: {skipped}")
    print(f"Errors Logged: {errors}\n")

if __name__ == "__main__":
    summarize_logs()
