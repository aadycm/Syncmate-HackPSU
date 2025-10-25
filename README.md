#  SyncMate — Smart File Synchronization Tool

**Built at HackPSU 2025**  
A lightweight, intelligent file synchronization system powered by Python and a touch of AI.

##  Overview

SyncMate is a Python-based application that keeps two folders perfectly in sync — like a mini dropbox.
It continuously monitors file changes using MD5 hashing, detects updates or new files, and synchronizes them automatically.  

This project demonstrates key concepts in systems programming**, file I/O, automation, and AI-based insights, wrapped in a clean Tkinter GUI for an interactive experience.

##  Features

- Automatic Folder Syncing — keeps source and destination folders identical in real time.  
- MD5 File Hashing — ensures file integrity and detects any change accurately.  
- Tkinter GUI — easy-to-use interface for selecting folders and managing sync sessions.  
- AI Log Summarizer — analyzes sync logs and gives short summaries or insights.  

---

## Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Language | Python 3.10+ |
| GUI | Tkinter |
| Hashing | hashlib |
| File Operations | os, shutil |
| Logging | Built-in logging |
| AI Summary | SentenceTransformers (MiniLM-L6-v2) |

---

##  How to Run

There are 3 modes available

### Command Line Mode

```bash
python3 SyncMate.py
```

You’ll be prompted to enter the source and destination folder paths.  
The script will automatically detect and copy new or modified files every 5 seconds.

---

### GUI Mode

```bash
python3 gui_app.py
```

From the interface, you can:
- Select source and destination folders  
- Start and stop sync manually  
- View realtime log output  

---

### AI Summary Mode

```bash
python3 ai_summary.py
```

It produces a concise analysis of the sync process, highlighting efficiency, issues, and suggestions.

---

##  Project Structure

```
SyncMate/
│
├── SyncMate.py          # Core backend sync logic
├── gui_app.py           # Tkinter-based GUI application
├── ai_summary.py        # AI-based log summarizer
├── sync_log.txt         # Auto-generated sync log file
└── README.md            # Project documentation
```

---

##  What I Built at HackPSU

For this project i used a pre-prepared file synchronization template (SyncMate.py) to quickly build a reliable backend.During HackPSU i extended it by adding a Tkinter GUI,AI-powered log summarization,real-time file monitoring, and detailed logging.

##  Future Improvements

- Add Google Drive or AWS S3 integration for cloud sync  
- Implement file versioning and recovery options  
- Add user authentication for multi-device syncing  

---

##  Inspiration

I wanted to create a project that bridges systems programming and AI, while remaining practical and understandable.  
SyncMate reflects my interest in building tools that automate repetitive tasks and make everyday computing simpler.

---

##  Built With

Python · Tkinter · hashlib · SentenceTransformers · shutil  

---

## Notes / Acknowledgements

- Some guidance for Tkinter UI improvements and AI summary integration was taken from online tutorials and AI assistants.

## Additional Information & Citations

**Project Ownership**: Core logic (file sync, GUI, AI summarization) was implemented by our team during HackPSU Fall 2025. We consulted ChatGPT and official documentation for guidance, debugging, and design improvements; all code was finalized and tested by us.

**References**:

Python documentation: tkinter, hashlib, shutil

SentenceTransformers library for AI summarization

ChatGPT for guidance on threading, GUI handling, and log summarization

**Open Source Packages**:

hashlib – file hashing

shutil – file copy/sync

tkinter – GUI

sentence-transformers – AI summarization

---

##  Authors

Name: Aadithya Chandramouli 

Teamates : Manmeet Singh Kukreja & Umang Virmani

Hackathon: HackPSU 2025  

Project: SyncMate — File Synchronization Tool  
