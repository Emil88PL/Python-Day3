import cowsay
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)  # 0 for male 1 for female

this = input("What you want me to say? ")

cowsay.cow(this)
engine.say(this)

engine.runAndWait()


engine.stop()