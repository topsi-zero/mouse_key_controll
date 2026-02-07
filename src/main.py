try:
    from pynput.mouse import Controller, Button
    from pynput.keyboard import Listener, Key
    PYNPUT_AVAILABLE = True
except (ImportError, Exception) as e:
    print(f"Warning: pynput not available ({e})")
    print("Running in simulator mode...\n")
    PYNPUT_AVAILABLE = False
    
    class Button:
        left = "LEFT"
        right = "RIGHT"
    
    class Key:
        up = "up"
        down = "down"
        left = "left"
        right = "right"
        enter = "enter"
        space = "space"
        esc = "esc"
    
    class Controller:
        def __init__(self):
            self.x = 0
            self.y = 0
        
        def move(self, x, y):
            self.x += x
            self.y += y
            print(f"  Move: ({x}, {y}) -> Position: ({self.x}, {self.y})")
        
        def click(self, button, times):
            print(f"  Click: {button} ({times}x)")
    
    class Listener:
        def __init__(self, on_press, on_release):
            self.on_press = on_press
            self.on_release = on_release
        
        def __enter__(self):
            return self
        
        def __exit__(self, *args):
            pass
        
        def join(self):
            import sys
            print("Simulator: Press keys (or type commands):")
            while True:
                try:
                    cmd = input("> ").strip().lower()
                    if cmd == "up":
                        self.on_press(Key.up)
                    elif cmd == "down":
                        self.on_press(Key.down)
                    elif cmd == "left":
                        self.on_press(Key.left)
                    elif cmd == "right":
                        self.on_press(Key.right)
                    elif cmd == "enter":
                        self.on_press(Key.enter)
                    elif cmd == "space":
                        self.on_press(Key.space)
                    elif cmd == "esc" or cmd == "exit":
                        self.on_press(Key.esc)
                        break
                    elif cmd:
                        print(f"Unknown command: {cmd}")
                except KeyboardInterrupt:
                    break

import time

mouse = Controller()

# Configuration
MOVE_DISTANCE = 10
MOVE_DELAY = 0.05

def on_press(key):
    try:
        if key == Key.up:
            mouse.move(0, -MOVE_DISTANCE)
        elif key == Key.down:
            mouse.move(0, MOVE_DISTANCE)
        elif key == Key.left:
            mouse.move(-MOVE_DISTANCE, 0)
        elif key == Key.right:
            mouse.move(MOVE_DISTANCE, 0)
        elif key == Key.enter:
            mouse.click(Button.left, 1)
        elif key == Key.space:
            mouse.click(Button.right, 1)
        elif key == Key.esc:
            return False  # Stop listener
    except AttributeError:
        pass

def on_release(key):
    pass

if __name__ == "__main__":
    print("Mouse Control Program")
    print("Arrow Keys: Move mouse")
    print("Enter: Left click")
    print("Space: Right click")
    print("ESC: Exit")
    print("-" * 40)
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("Program ended.")