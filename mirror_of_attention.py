import time
import pygetwindow as gw
from datetime import datetime
import os

LOG_FILE = "attention_log.csv"

# Create log file with headers if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("timestamp,window,duration_seconds\n")

last_window = None
last_time = time.time()

print("Attention tracker started.")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        active = gw.getActiveWindow()

        if active is not None:
            current_window = active.title.strip()
            current_time = time.time()

            # Window changed
            if current_window != last_window:
                if last_window is not None:
                    duration = current_time - last_time
                    timestamp = datetime.now().isoformat(timespec="seconds")

                    with open(LOG_FILE, "a", encoding="utf-8") as f:
                        f.write(f"{timestamp},{last_window},{duration:.2f}\n")

                    print(f"Switched from '{last_window}' after {duration:.2f} seconds")

                last_window = current_window
                last_time = current_time
                print(f"Now on: {current_window}")

        time.sleep(0.5)  # check twice per second

except KeyboardInterrupt:
    print("\nTracking stopped.")
