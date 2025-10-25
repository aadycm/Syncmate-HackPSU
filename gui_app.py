import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import threading
import time
import os
import SyncMate  # Make sure SyncMate.py is in the same folder

running = False

def start_sync():
    global running
    running = True

    src = src_entry.get().strip()
    dst = dst_entry.get().strip()

    if not os.path.exists(src):
        messagebox.showerror("Error", "Source folder does not exist.")
        return

    os.makedirs(dst, exist_ok=True)
    log_text.insert(tk.END, f"Starting sync from {src} → {dst}\n")
    log_text.see(tk.END)

    def sync_loop():
        while running:
            try:
                summary = SyncMate.sync_folders(src, dst)
                with open("sync_log.txt", "a") as f:
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {summary}\n")
                log_text.insert(tk.END, summary + "\n")
                log_text.see(tk.END)
            except Exception as e:
                err_msg = f"Error: {str(e)}"
                with open("sync_log.txt", "a") as f:
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {err_msg}\n")
                log_text.insert(tk.END, err_msg + "\n")
            time.sleep(5)

    threading.Thread(target=sync_loop, daemon=True).start()

def stop_sync():
    global running
    running = False
    log_text.insert(tk.END, "Sync stopped.\n")
    log_text.see(tk.END)

def browse_src():
    folder = filedialog.askdirectory()
    if folder:
        src_entry.delete(0, tk.END)
        src_entry.insert(0, folder)

def browse_dst():
    folder = filedialog.askdirectory()
    if folder:
        dst_entry.delete(0, tk.END)
        dst_entry.insert(0, folder)

# GUI setup
root = tk.Tk()
root.title("SyncMate — File Synchronizer")
root.geometry("650x450")

tk.Label(root, text="Source Folder:").pack(pady=(10, 0))
src_entry = tk.Entry(root, width=60)
src_entry.pack()
ttk.Button(root, text="Browse", command=browse_src).pack(pady=5)

tk.Label(root, text="Destination Folder:").pack(pady=(10, 0))
dst_entry = tk.Entry(root, width=60)
dst_entry.pack()
ttk.Button(root, text="Browse", command=browse_dst).pack(pady=5)

ttk.Button(root, text="Start Sync", command=start_sync).pack(pady=10)
ttk.Button(root, text="Stop Sync", command=stop_sync).pack(pady=5)

log_text = scrolledtext.ScrolledText(root, width=75, height=15)
log_text.pack(pady=10)

root.mainloop()
