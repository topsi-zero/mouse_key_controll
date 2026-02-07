import sys
import time
from threading import Thread
from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode

# src/main.py
# Simple mouse control using keyboard (WASD or arrow keys). Press ESC to exit.
# Requires: pip install pynput


MOUSE_INTERVAL = 0.01  # seconds between moves
BASE_SPEED = 15        # pixels per interval

mouse_ctrl = mouse.Controller()
pressed = set()
running = True


def key_to_name(key):
    if isinstance(key, KeyCode):
        return key.char
    return key


def on_press(key):
    global running
    k = key_to_name(key)
    pressed.add(k)
    if k == Key.esc:
        running = False
        return False  # stop listener


def on_release(key):
    k = key_to_name(key)
    if k in pressed:
        pressed.remove(k)


def mover_loop():
    while running:
        dx = dy = 0
        speed = BASE_SPEED

        # acceleration while shift held
        if Key.shift in pressed or 'shift' in pressed:
            speed *= 3

        # WASD or arrow keys
        if 'w' in pressed or Key.up in pressed:
            dy -= speed
        if 's' in pressed or Key.down in pressed:
            dy += speed
        if 'a' in pressed or Key.left in pressed:
            dx -= speed
        if 'd' in pressed or Key.right in pressed:
            dx += speed

        if dx != 0 or dy != 0:
            try:
                mouse_ctrl.move(int(dx), int(dy))
            except Exception:
                pass

        time.sleep(MOUSE_INTERVAL)


def main():
    print("Mouse control active. Use WASD or arrow keys to move. Hold Shift to speed up. ESC to quit.")
    mover = Thread(target=mover_loop, daemon=True)
    mover.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print("Exiting.")


if __name__ == "__main__":
    main()