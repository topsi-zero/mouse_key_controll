import threading
import keyboard as key
from pynput import keyboard

def main():
    print("Mouse control active. Use WASD or arrow keys to move. Hold Shift to speed up. Q/E for left/right click. ESC to quit.")
    mover = threading.Thread(target = key.mover_loop, daemon=True)
    mover.start()

    with keyboard.Listener(on_press = key.on_press, on_release = key.on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()