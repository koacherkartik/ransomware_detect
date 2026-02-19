from watchdog.events import FileSystemEventHandler
from collections import deque
import time
from detector.entropy_detector import calculate_entropy

HIGH_ENTROPY_THRESHOLD = 7.2
MODIFICATION_THRESHOLD = 15
TIME_WINDOW = 5  # seconds

class RansomwareDetector(FileSystemEventHandler):
    def __init__(self):
        self.events = deque()

    def on_moved(self, event):
        if event.is_directory:
            return

        entropy = calculate_entropy(event.dest_path)
        if entropy >= HIGH_ENTROPY_THRESHOLD:
            print(f"[HIGH] Encrypted file detected: {event.dest_path} | Entropy: {entropy}")

        current_time = time.time()
        self.events.append(current_time)
        while self.events and current_time - self.events[0] > TIME_WINDOW:
            self.events.popleft()

        if len(self.events) >= MODIFICATION_THRESHOLD:
            print("[MEDIUM] High volume of file modifications detected")
