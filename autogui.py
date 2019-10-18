import pyautogui


def record_track_one():
    pyautogui.click(x=63, y=647, clicks=1, duration=0)


def create_command(phrase, mouse_x, mouse_y):
    '''creates command from user's phrase,and mouse coordinates:\n phrase = str\n mouse_x = int\n mouse_y = int\n returns: list of phrases'''
    parsed_phrase = f"""{phrase},{mouse_x},{mouse_y}"""
    phrase_list = parsed_phrase.split(",")
    return phrase_list
