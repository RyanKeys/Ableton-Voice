import speech_recognition as sr
import autogui
import sys
import pyautogui

start_prompt = 'Ableton Voice V.1.0\nReady for a command:'

commands = []
# Creates an instance of Recognizer(), detects voice input
r = sr.Recognizer()
# TODO: allows users to choose input devices
# receives audio from users first mic
mic = sr.Microphone()
with mic as source:
    # checks for commands
    while True:
        r.adjust_for_ambient_noise(source)
        print(start_prompt)
        try:
            audio = r.listen(source)
            audio_str = r.recognize_google(audio)
            print(audio_str)
            # Start command is yo
            # Use if " " in audio_str to call code
            if "record first track" in audio_str:
                autogui.record_track_one()
            elif "create a command" in audio_str:
                create_command = autogui.create_command()
                command = create_command.split()
                commands.append(command)
                x_pos = int(command[1])
                y_pos = int(command[2])
                print(commands)
            elif command[0] in audio_str:
                pyautogui.click(x=x_pos, y=y_pos,
                                clicks=1, duration=0)

        except sr.UnknownValueError:
            print("Say that again?")
