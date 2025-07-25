import speech_recognition as sr
import webbrowser 
import pyttsx3
import songslibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
import pygame
import os
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open chatGPT" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link = songslibrary.songs[song]
        webbrowser.open(link) 
        speak(f"Playing {song}")
    else:
        pass
 
if __name__ == "__main__":
    speak("Initilizing Jarvis")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("ya")
                #listen command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.WaitTimeoutError:
            print("Timeout — No speech detected.")
        except Exception as e:
            print("Error:", e)