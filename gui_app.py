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
    source = source_entry.get().strip()
    destination = destination_entry.get().strip()

    # If condition to check if source file does not exist then print an error statement
    if not os.path.exists(source):
        messagebox.showerror("Error, Source folder does not exist")
        return

    # If the file exists, make a destination directory
    os.makedirs(destination,exist_ok=True)
    log_text.insert(tk.END, f"Starting sync from {source} to {destination}\n")
    log_text.see(tk.END)

    # This function starts syncing files from source to destination
    def sync_loop():
        # While loop to keep the sync running until user clicks stop sync
        while flag:
            # Try and except block to handle any unexpected errors
            try:
                summary = SyncMate.sync_folders(source,destination)

                # Opens the sync log.txt to append mode to append the current log into the file
                with open("sync_log.txt", "a") as file:
                    file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {summary}\n")
                log_text.insert(tk.END, summary + "\n")
                log_text.see(tk.END)
            except Exception as e:
                err_msg = f"Error:{str(e)}"
                with open("sync_log.txt","a") as file:
                    file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {err_msg}\n")
                log_text.insert(tk.END,err_msg + "\n")
            time.sleep(5)

    # This line creates a new sync process by creating a new thread
    threading.Thread(target=sync_loop,daemon=True).start()

# This function stops the syncing process and logs the current process into sync_log.txt file
def stop_sync():        
    global flag
    flag = False
    log_text.insert(tk.END,"Sync stopped\n")
    log_text.see(tk.END)

# This function allows the user to select a source folder to be synced
def browse_source():
    folder = filedialog.askdirectory()
    if folder:
        source_entry.delete(0,tk.END)
        source_entry.insert(0,folder)

# This function allows the user to select a destination folder where the source folder files would be synced to
def browse_destination():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0,tk.END)
        destination_entry.insert(0,folder)

# This block creates a GUI environment for user and places labels, text boxes, and buttons
root = tk.Tk()
root.title("SyncMate — File Synchronizer")
root.geometry("700x500")
tk.Label(root,text="Source Folder:").pack(pady=(10, 0))
source_entry = tk.Entry(root,width=60)
source_entry.pack()
ttk.Button(root,text="Browse",command=browse_source).pack(pady=5)
tk.Label(root,text="Destination Folder:").pack(pady=(10,0))
destination_entry = tk.Entry(root,width=60)
destination_entry.pack()
ttk.Button(root,text="Browse",command=browse_destination).pack(pady=5)
ttk.Button(root,text="Start Sync",command=start_sync).pack(pady=10)
ttk.Button(root,text="Stop Sync",command=stop_sync).pack(pady=5)
log_text = scrolledtext.ScrolledText(root,width=75,height=15)
log_text.pack(pady=10)

root.mainloop()

