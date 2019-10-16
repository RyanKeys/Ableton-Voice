import speech_recognition as sr


# Creates an instance of Recognizer(), detects voice input
r = sr.Recognizer()
# TODO: allows users to choose input devices
# receives audio from users first mic
mic = sr.Microphone()
with mic as source:
    # checks for commands
    while True:
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        try:
            audio = r.listen(source)
            audio_str = r.recognize_google(audio)

            # start command is yo
            if "yo" in audio_str:
                r.adjust_for_ambient_noise(source)
                print("command works")

        except sr.UnknownValueError:
            print("Say that again?")
