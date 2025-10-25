import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
import threading
import time
import os
import SyncMate

flag = False

def start_sync():
    global flag
    flag = True
    src = src_entry.get().strip()
    dst = dst_entry.get().strip()
    if not os.path.exists(src): # Condition to check if the source file exists in the computer or not, if not then display an error message
        messagebox.showerror("Error", "Source folder does not exist")
        return
    os.makedirs(dst, exist_ok=True) # If file exists, create a desination folder and make sure it exists
    log_text.insert(tk.END, f"Starting sync from {src} → {dst}\n")
    log_text.see(tk.END)

    def sync_loop():            # Function that keeps syncing the file every 5 seconds until user clicks 'stop sync'
        while flag:         # while loop to keep the syncing process running until stopped by user
            try:         # Try-except block to prevent the loop from crashing if an error comes in the process
                summary = SyncMate.sync_folders(src, dst)           
                with open("sync_log.txt", "a") as f:         # opens a file called sync_log.txt in append mode
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {summary}\n")      # writes a timestamped log entry into that file
                log_text.insert(tk.END, summary + "\n")
                log_text.see(tk.END)
            except Exception as e:      # If any error occurs, shows an error message and appends it in the log
                err_msg = f"Error: {str(e)}"
                with open("sync_log.txt", "a") as f:
                    f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {err_msg}\n")
                log_text.insert(tk.END, err_msg + "\n")
            time.sleep(5)
    threading.Thread(target=sync_loop, daemon=True).start()         # This creates a new thread in Python to start a new syncing process

def stop_sync():        # This function executes if the user clicks 'stop sync' and appends in the log that 'Sync stopped'
    global flag
    flag = False
    log_text.insert(tk.END, "Sync stopped.\n")
    log_text.see(tk.END)

def browse_src():       # Function to allow the user to select a source folder using GUI dialog box
    folder = filedialog.askdirectory()
    if folder:
        src_entry.delete(0, tk.END)
        src_entry.insert(0, folder)

def browse_dst():       # Function to allow the user to select a destination folder using GUI dialog box
    folder = filedialog.askdirectory()
    if folder:
        dst_entry.delete(0, tk.END)
        dst_entry.insert(0, folder)

# This block creates a GUI environment for user and places labels, text boxes, and buttons
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

