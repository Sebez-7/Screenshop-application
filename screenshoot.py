import time
import pyautogui
import os
import tkinter as tk

def screenshot():
    # Create timestamp for filename
    timestamp = int(round(time.time() * 1000))
    folder_path = r"C:\Users\Monoshot Thinker\Desktop\AI\20 projects\screenshot\images"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{timestamp}.png")

    time.sleep(2)  # Short delay to allow you to adjust the screen
    img = pyautogui.screenshot(file_path)
    img.show()

# Create Tkinter window
root = tk.Tk()
root.title("Screenshot Tool")

frame = tk.Frame(root)
frame.pack()

# Take Screenshot Button
button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT)

# Quit Button
close = tk.Button(frame, text="QUIT", command=root.quit)
close.pack(side=tk.LEFT)

root.mainloop()
# Ensure the script runs only if it's the main module
if __name__ == "__main__":
    root.mainloop()