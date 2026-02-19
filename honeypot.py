from watchdog.events import FileSystemEventHandler

class HoneypotHandler(FileSystemEventHandler):
    def __init__(self, decoy_files):
        self.decoy_files = set(decoy_files)

    def on_modified(self, event):
        if event.src_path in self.decoy_files:
            print(f"[CRITICAL] Honeypot file modified: {event.src_path}")

    def on_moved(self, event):
        if event.src_path in self.decoy_files:
            print(f"[CRITICAL] Honeypot file renamed: {event.src_path}")
