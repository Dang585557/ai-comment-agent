import pyautogui
import pyperclip
import time
from pathlib import Path


class DesktopAgent:

    def __init__(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.2

    def move(self, x: int, y: int):
        pyautogui.moveTo(x, y)

    def click(self, x=None, y=None):
        pyautogui.click(x=x, y=y)

    def double_click(self, x=None, y=None):
        pyautogui.doubleClick(x=x, y=y)

    def right_click(self, x=None, y=None):
        pyautogui.rightClick(x=x, y=y)

    def drag(self, x: int, y: int):
        pyautogui.dragTo(x, y, duration=0.5)

    def scroll(self, amount: int):
        pyautogui.scroll(amount)

    def write(self, text: str):
        pyautogui.write(text)

    def paste(self, text: str):
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)

    def press(self, key: str):
        pyautogui.press(key)

    def screenshot(self, filename="desktop.png"):
        path = Path(filename)
        pyautogui.screenshot(str(path))
        return str(path)

    def locate(self, image_path: str, confidence=0.8):
        return pyautogui.locateCenterOnScreen(
            image_path,
            confidence=confidence
        )

    def click_image(self, image_path: str, confidence=0.8):

        pos = self.locate(image_path, confidence)

        if pos:
            pyautogui.click(pos)
            return True

        return False

    def size(self):
        return pyautogui.size()

    def position(self):
        return pyautogui.position()

    def wait(self, seconds):
        time.sleep(seconds)


if __name__ == "__main__":

    agent = DesktopAgent()

    print(agent.size())
