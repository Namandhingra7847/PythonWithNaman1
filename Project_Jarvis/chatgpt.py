import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import requests
import os
from gtts import gTTS
import pygame
import time

# Replace with your OpenAI API Key
openai.api_key = 'your-openai-api-key'

# Initialize pyttsx3 engine
engine = pyttsx3.init()
pygame.init()

# Speak text using pyttsx3
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        # If pyttsx3 fails, fallback to gTTS
        tts = gTTS(text=text, lang='en')
        filename = "voice.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.2)
        os.remove(filename)

# Listen for voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# Handle OpenAI GPT queries
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I couldn't reach OpenAI."

# News fetching using NewsAPI (replace with your key if you want more)
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=demo"  # Use your NewsAPI key here
    try:
        res = requests.get(url)
        articles = res.json()['articles'][:5]
        news = "Here are the top news headlines:\n"
        for article in articles:
            news += "- " + article['title'] + "\n"
        return news
    except:
        return "Unable to fetch news."

# Process commands
def process_command(command):
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "news" in command:
        news = get_news()
        print(news)
        speak(news)
    elif "play song" in command:
        webbrowser.open("https://open.spotify.com/")
        speak("Opening Spotify.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye.")
        exit()
    else:
        response = ask_openai(command)
        print(f"Jarvis: {response}")
        speak(response)

# Main loop
def main():
    speak("Initializing Jarvis...")
    while True:
        command = listen()
        if "jarvis" in command:
            speak("Ya")
            command = listen()
            process_command(command)

if __name__ == "__main__":
    main()
