import threading
import time
from pynput import keyboard
import pyautogui
import random
import pync
from pync import Notifier

jiggler_running = False

def executable():

    def mouse_jiggler_function(movement_distance=10, interval=0.5):
        global jiggler_running
        screen_width, screen_height = pyautogui.size()

        # Initial delay with periodic checks to allow immediate stopping
        for _ in range(7):
            if not jiggler_running:
                return
            time.sleep(1)

        if not jiggler_running:
            return

        for _ in range(3):
            if not jiggler_running:
                return
            time.sleep(1)
        
        for remaining in range(3, 0, -1):
            if not jiggler_running:
                return
            Notifier.notify(f'Time remaining: {remaining} seconds', title='Jiggler')
            time.sleep(1)
        
        if not jiggler_running:
            return
        
        Notifier.notify('Jiggler Starting Now', title='Jiggler')

        time.sleep(1)
        
        pyautogui.moveTo(screen_width / 2, screen_height / 2)
        pyautogui.click()

        while jiggler_running:
            random_distance_x = random.randint(-movement_distance, movement_distance)
            random_distance_y = random.randint(-movement_distance, movement_distance)

            pyautogui.moveRel(random_distance_x, random_distance_y, duration=0.25)
            time.sleep(interval)

    def start_jiggler():
        global jiggler_running
        if not jiggler_running:
            jiggler_running = True
            threading.Thread(target=mouse_jiggler_function).start()
            pync.notify(
                title='Jiggler', 
                message='In 10 seconds Jiggler will center, click and start jiggling!', 
                sound='default'
            )
        else:
            pync.notify(
                title='Jiggler', 
                message='Mouse Jiggler is already running', 
                sound='default'
            )

    def stop_jiggler():
        global jiggler_running
        if jiggler_running:
            jiggler_running = False
            pync.notify(
                title='Jiggler', 
                message='Mouse Jiggler stopping', 
                sound='default'
            )
        else:
            pync.notify(
                title='Jiggler', 
                message='Mouse Jiggler is not running', 
                sound='default'
            )

    def on_press(key):
        try:
            if key == keyboard.Key.cmd:
                on_press.cmd_pressed = True
            elif key == keyboard.Key.shift:
                on_press.shift_pressed = True
            elif key.char == 'u' and on_press.cmd_pressed and on_press.shift_pressed:
                start_jiggler()
            elif key.char == 'k' and on_press.cmd_pressed and on_press.shift_pressed:
                stop_jiggler()
        except AttributeError:
            pass

    def on_release(key):
        if key == keyboard.Key.cmd:
            on_press.cmd_pressed = False
        elif key == keyboard.Key.shift:
            on_press.shift_pressed = False

    # Initialize state variables
    on_press.cmd_pressed = False
    on_press.shift_pressed = False

    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    executable()