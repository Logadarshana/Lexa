import pygame
import pyttsx3
import speech_recognition as sr
import os
import sys

# Initialize pygame mixer
pygame.mixer.init()

# Path to the directory containing songs
path = "C:\\LEXA- MUSIC ASSISTANT\\"
songs = [os.path.join(path, song) for song in os.listdir(path) if song.endswith('.mp3')]

# Initialize speech recognition and text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Set voice and rate
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

engine.say("HI! I'M LEXA, WHAT CAN I PLAY FOR YOU?")
engine.runAndWait()

while True:
    query = ""
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-US")
        print(f"Query: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        continue
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        continue

    if "play" in query.lower():
        if "play my favourite" in query.lower():
            print("\nPlaying your favourite music\n")
            engine.say("Playing your favourite music")
            engine.runAndWait()
            pygame.mixer.music.load(os.path.join(path, "What-a-Karavaad.mp3"))
            pygame.mixer.music.play()
            
        else:
            for song in songs:
                if query.lower().strip().startswith("play "):
                    song_name = query[5:].lower()
                    if song_name in song.lower():
                        print(f"\nPlaying {song_name}\n")
                        engine.say(f"Playing {song_name}")
                        engine.runAndWait()
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.play()
                        break

    elif "stop" in query.lower():
        pygame.mixer.music.stop()
        engine.say("Music stopped")
        engine.runAndWait()

    elif "unpause" in query.lower():
        engine.say("Music unpaused")
        engine.runAndWait()
        pygame.mixer.music.unpause()

    elif "pause" in query.lower():
        engine.say("Music paused")
        engine.runAndWait()
        pygame.mixer.music.pause()

    elif "shutdown" in query.lower():
        pygame.mixer.music.stop()
        engine.say("Shutting down, Goodbye!!")
        engine.runAndWait()
        sys.exit()

        
        



    




