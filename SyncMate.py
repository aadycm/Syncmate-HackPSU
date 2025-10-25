import os
import hashlib
import shutil
import time

def hash_file(path):
    """Return MD5 hash of a file's content."""
    with open(path, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

def sync_folders(src, dst):
    """Synchronize files from the source folder to the destination folder."""
    copied = 0
    updated = 0
    skipped = 0
    errors = 0

    for root, dirs, files in os.walk(src):
        for file in files:
            try:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src)
                dst_path = os.path.join(dst, rel_path)

                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                # copy new or modified files
                if not os.path.exists(dst_path):
                    shutil.copy2(src_path, dst_path)
                    copied += 1
                elif hash_file(src_path) != hash_file(dst_path):
                    shutil.copy2(src_path, dst_path)
                    updated += 1
                else:
                    skipped += 1
            except Exception as e:
                errors += 1

    summary = f"Sync done | New: {copied}, Updated: {updated}, Skipped: {skipped}, Errors: {errors}"
    print(summary)
    return summary

def main():
    src = input("Enter source folder path: ").strip()
    dst = input("Enter destination folder path: ").strip()

    if not os.path.exists(src):
        print("Source folder does not exist.")
        return

    os.makedirs(dst, exist_ok=True)
    print("Starting file synchronization. Press Ctrl+C to stop.")

    try:
        while True:
            sync_folders(src, dst)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Sync stopped by user.")

if __name__ == "__main__":
    main()
