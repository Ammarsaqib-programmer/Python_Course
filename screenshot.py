import time
import pyautogui
import tkinter as tk
import os

def screenshot():
    try:
        save_dir = 'D:/Python/screenshots data/'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        name = int(round(time.time() * 1000))
        filepath = f"{save_dir}{name}.png"

        img = pyautogui.screenshot(filepath)
        img.show()  
        print(f"Screenshot saved at {filepath}")
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Screenshot App")
root.geometry("300x100")  

frame = tk.Frame(root)
frame.pack(pady=20)

screenshot_button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
screenshot_button.pack(side=tk.LEFT, padx=10)

quit_button = tk.Button(
    frame,
    text="QUIT",
    command=root.destroy  
)
quit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
