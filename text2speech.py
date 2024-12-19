import pyttsx3

data = input("enter the text for speech")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()