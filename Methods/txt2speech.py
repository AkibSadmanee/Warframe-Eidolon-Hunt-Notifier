def read(string):
    import pyttsx3
    engine = pyttsx3.init()
    
    engine.say(string)
    engine.runAndWait()