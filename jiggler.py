import pyautogui
import fastapi
import uvicorn
import time

app = fastapi.FastAPI()

# Global variables to control the jiggler thread
jiggler_running = False

def mouse_jiggler_function(movement_distance=20, interval=0.5):
    global jiggler_running
    screen_width, screen_height = pyautogui.size()

    time.sleep(10)

    pyautogui.moveTo(screen_width / 2, screen_height / 2)

    pyautogui.click()
    
    while jiggler_running:
        pyautogui.moveRel(movement_distance, 0, duration=0.25)  # Move right
        pyautogui.moveRel(0, movement_distance, duration=0.25)  # Move up
        time.sleep(interval)
        pyautogui.moveRel(-movement_distance, 0, duration=0.25)  # Move left
        pyautogui.moveRel(0, -movement_distance, duration=0.25)  # Move down
        time.sleep(interval)

@app.get("/")
def return_info():
    return {"Mouse Jiggler is running, navigate to /jiggle to start jiggling and /stop to stop jiggling."}

@app.get("/jiggle")
def mouse_jiggler():
    global jiggler_running
    if jiggler_running == False:
        jiggler_running = True
        mouse_jiggler_function()
        return {"status": "Jiggler started!"}
    else:
        return {"status": "Jiggler is already running!"}

@app.get("/stop")
def stop_jiggler():
    global jiggler_running
    if jiggler_running:
        jiggler_running = False
        return {"status": "Jiggler stopped!"}
    else:
        return {"status": "Jiggler is not running!"}
    
def handle_keyboard_interrupt():
    global jiggler_running
    jiggler_running = False
    print("Keyboard interrupt received. Stopping jiggler...")

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        handle_keyboard_interrupt()