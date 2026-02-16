from pynput import mouse

mouse_ctrl = mouse.Controller()


def on_move(x, y):
    mouse_ctrl.move(x, y)