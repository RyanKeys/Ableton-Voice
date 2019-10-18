import speech_recognition as sr
import autogui
import pyautogui

start_prompt = 'Ableton Voice V.1.0\nReady for a command:'
commands = ["test", 1, 1]
command_output = 'N/A'

# Creates an instance of Recognizer(), detects voice input
r = sr.Recognizer()

# receives audio from users first mic
mic = sr.Microphone()

with mic as source:
    while True:
        r.adjust_for_ambient_noise(source)
        print(start_prompt)

        try:
            audio = r.listen(source)
            audio_str = r.recognize_google(audio)
            print(audio_str)

            # Use if " " in audio_str to call code
            if "record first track" in audio_str:
                autogui.record_track_one()

            # asks the user to create a command phrase and choose its x and y coordinates
            elif "create a command" in audio_str:
                phrase = str(input("Choose a command phrase:"))
                mouse_x = int(input("Choose a X coordinate:"))
                mouse_y = int(input("Choose a Y coordinate:"))
                # create a command using autogui
                command_output = autogui.create_command(
                    phrase, mouse_x, mouse_y)

            elif 'show commands' in audio_str:
                print(f"{commands}")

            # command_phrase[0] == user's previously input str
            elif command_output[0] in audio_str:
                pyautogui.click(x=mouse_x, y=mouse_y,
                                clicks=1, duration=0)
            else:
                pass
        except sr.UnknownValueError:
            print("Say that again?")
