import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key_Code

TOGGLE_KEY = Key_Code(char="s")

clicking = False

mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()

with Listener(on_press=toggle_event) as Listener:
    listener.join()