import pyautogui
import time
import pyperclip

# Step 1: Small delay to let you prepare
print("You have 3 seconds to prepare...")
time.sleep(3)

# Step 2: Click the whatsapp icon to open or focus
pyautogui.click(1047, 914)
time.sleep(1)  # wait for the app to open

# Step 3: Drag to select text
pyautogui.moveTo(639, 209)
pyautogui.dragTo(622,820, duration=0.5, button='left')  # drag with left button

time.sleep(0.5)

# Step 4: Press Ctrl+C to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 5: Get clipboard content
copied_text = pyperclip.paste()

# Step 6: Show result
print("Copied Text:")
print(copied_text)
