import keyboard
import time
import threading
import os
from pystyle import *

os.system("cls")

os.system(f"title Clicker - MADE by: Egwyl666")

banner = """
The script is running. Waiting for pressing 'n' to start pressing and 'f' to stop.
"""

print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
Write.Print("[+] Starting Clicker", Colors.blue_to_purple, interval=0.04)
print()


def press_key_with_interval(key, interval):
    """Function for automatic key presses at a set interval."""
    while running:
        if keyboard.is_pressed('f'):  # If the 'F' key is pressed, stop the presses
            break
        keyboard.press_and_release(key)
        time.sleep(interval)


def monitor_keys():
    """Function for monitoring 'n' and 'f' key presses."""
    global running
    while active:
        if keyboard.is_pressed('n') and not running:
            running = True
            threading.Thread(target=press_key_with_interval,
                             args=('e', 0.1)).start()
        elif keyboard.is_pressed('f') and running:
            running = False
            print("The taps have stopped.")
        # Add a small delay to prevent multiple triggers
        time.sleep(0.1)


# Initialise flags
running = False  # Controls automatic presses
active = True  # Manages the main monitoring cycle
# Run key monitoring in a separate thread
threading.Thread(target=monitor_keys).start()

print("The script is running. Waiting for pressing 'n' to start pressing and 'f' to stop.")
