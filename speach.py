import cowsay
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 

this = input("Whta's this? ")
cowsay.cow(this)
engine.say(this)

engine.runAndWait()


engine.stop()