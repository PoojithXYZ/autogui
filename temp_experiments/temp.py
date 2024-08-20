import pyautogui
import time
import pyperclip

def move_and_click(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()

def type_text(text):
    pyautogui.write(text, interval=0.1)

def get_submissions(problem_link):
    try:
        time.sleep(6)
        pyautogui.hotkey('win', 'up')  # Assuming "thehive" is the top window
        move_and_click(350, 250)
        pyautogui.hotkey('ctrl', 's')
        pyautogui.hotkey('win', 'd')  # Assuming "all files" is on the desktop
        type_text("hive_file_mhtml")
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl')
        time.sleep(2.5)
        pyautogui.hotkey('win', 'up')  # Bring "thehive" back to front
        pyautogui.hotkey('win', 'r')
        type_text(problem_link)
        pyautogui.press('enter')
        time.sleep(6)
        pyautogui.hotkey('win', 'up')  # Bring "thehive" back to front
        for _ in range(5):
            move_and_click(800, 550)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        # Save clipboard content to file
        temp = "temp.py"  # Replace with your desired filename
        with open(f"si_solutions/raw_code/{temp}", "w") as f:
            f.write(pyperclip.paste())
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
problem_link = "https://hive.smartinterviews.in/submission/661516fb96bb0dcd9cd46cb0"
get_submissions(problem_link)
