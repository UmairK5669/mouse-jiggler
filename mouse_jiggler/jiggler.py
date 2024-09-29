import threading
import time
from pynput import keyboard, mouse
import pyautogui
import random
import pync
from pync import Notifier

jiggler_running = False
manual_movement_detected = False
movement_threshold = 10  # Threshold for detecting manual movement

def executable():

    def mouse_jiggler_function(movement_distance=10, interval=0.5):
        global jiggler_running, manual_movement_detected
        screen_width, screen_height = pyautogui.size()

        # Prevent movement near borders
        border_offset = 175

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

        # Move the mouse to the center with border restrictions
        pyautogui.moveTo(screen_width / 2, screen_height / 2)
        pyautogui.click()

        last_mouse_pos = pyautogui.position()

        while jiggler_running:
            current_mouse_pos = pyautogui.position()
            distance_moved = ((current_mouse_pos[0] - last_mouse_pos[0])**2 + (current_mouse_pos[1] - last_mouse_pos[1])**2)**0.5

            if distance_moved > movement_threshold:
                manual_movement_detected = True
                last_mouse_pos = current_mouse_pos
                time.sleep(1)  # Delay before checking again to avoid constant toggling
                continue

            if manual_movement_detected:
                manual_movement_detected = False
                time.sleep(3)  # Give some time before resuming jiggling

            # Constrain mouse movement within borders
            random_distance_x = random.randint(-movement_distance, movement_distance)
            random_distance_y = random.randint(-movement_distance, movement_distance)

            new_x = max(border_offset, min(screen_width - border_offset, last_mouse_pos[0] + random_distance_x))
            new_y = max(border_offset, min(screen_height - border_offset, last_mouse_pos[1] + random_distance_y))

            pyautogui.moveTo(new_x, new_y, duration=0.25)
            last_mouse_pos = pyautogui.position()  # Update last_mouse_pos after jiggler movement
            time.sleep(interval)

    def press_random_keys():
        while jiggler_running:
            # Randomly press Cmd + '+' and Cmd + '-' after intervals
            num_plus_presses = random.randint(0, 3)
            interval_between_plus = random.randint(60, 300)  # 1 to 5 minutes
            print(num_plus_presses, interval_between_plus)

            time.sleep(interval_between_plus)  # Wait before pressing Cmd + '+'
            for _ in range(num_plus_presses):
                pyautogui.hotkey('command', '+')
                time.sleep(0.2)

            time.sleep(random.randint(0, 180))  # Wait between 0 to 3 minutes before Cmd + '-'
            for _ in range(num_plus_presses):
                pyautogui.hotkey('command', '-')
                time.sleep(0.2)

            # Press Shift at random intervals
            shift_interval = random.randint(60, 300)  # 1 to 5 minutes
            time.sleep(shift_interval)
            pyautogui.press('shift')

            # Press Delete at random intervals
            delete_interval = random.randint(60, 300)  # 1 to 5 minutes
            time.sleep(delete_interval)
            pyautogui.press('delete')

    def start_jiggler():
        global jiggler_running
        if not jiggler_running:
            jiggler_running = True
            threading.Thread(target=mouse_jiggler_function).start()
            threading.Thread(target=press_random_keys).start()
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
