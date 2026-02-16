from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button
import mouse
import time

MOUSE_INTERVAL = 0.01
BASE_SPEED = 5

pressed = set()
running = True


def key_to_name(key):
    if isinstance(key, KeyCode):
        return key.char.lower() if key.char else None
    elif isinstance(key, Key):
        return key.name  # gives "shift", "up", etc.
    return None


def on_press(key):
    global running
    k = key_to_name(key)
    if not k:
        return

    pressed.add(k)

    if k == 'esc':
        running = False
        return False

    if k == 'q':
        mouse.mouse_ctrl.click(Button.left, 1)

    if k == 'e':
        mouse.mouse_ctrl.click(Button.right, 1)


def on_release(key):
    k = key_to_name(key)
    if not k:
        return

    pressed.discard(k)   # discard is safer than remove



def mover_loop():
    while running:
        dx = dy = 0.0
        speed = BASE_SPEED

        if 'shift' in pressed:
            speed *= 3

        if 'w' in pressed or 'up' in pressed:
            dy -= speed
        if 's' in pressed or 'down' in pressed:
            dy += speed
        if 'a' in pressed or 'left' in pressed:
            dx -= speed
        if 'd' in pressed or 'right' in pressed:
            dx += speed


        try:
            if dx != 0 or dy != 0:
                mouse.on_move(dx, dy)
            else:
                mouse.on_move(0, 0)
        except Exception:
            pass

        time.sleep(MOUSE_INTERVAL)