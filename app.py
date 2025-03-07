import pyttsx3

engine = pyttsx3.init()  # Initialize the speech engine

print("Welcome TO ROBOSPEAKER 1.2 created by Sabbir")

while True:
    s = input("What You Want To Speak: ")

    if s == "q":
        break

    engine.say(s)  # Speak the text
    engine.runAndWait()  # Wait until speech is finished
