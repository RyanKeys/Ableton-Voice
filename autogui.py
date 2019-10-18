import pyautogui


def record_track_one():
    pyautogui.click(x=63, y=647, clicks=1, duration=0)


def create_command():
    phrase = input("Choose a command Phrase:")
    mouse_x = input("X Coordinate:")
    mouse_y = input("Y Coordinate:")
    phrase_str = f"""{phrase} {mouse_x} {mouse_y}"""
    return phrase_str
