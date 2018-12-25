def text_to_speech(text: str):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    engine.say(text)
    engine.runAndWait()


# text_to_speech("Command Successfully Executed!")
# text_to_speech("Here you go!")