import speech_recognition as sr
import pyttsx3
import webbrowser
import pygame
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

def search(query):
    query = query.replace("search", "")
    query = query.strip()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("D:\music")
    pygame.mixer.music.play()

def schedule_task():
    now = datetime.datetime.now()
    speak(f"The current date and time is {now}. What task would you like to schedule?")
    task = listen()
    # Implement your scheduling logic here

while True:
    command = listen().lower()
    
    if "hello" in command:
        speak("Hello there!")
        
    elif "goodbye" in command:
        speak("Goodbye! Take care.")
        break
        
    elif "search" in command:
        search(command)
        
    elif "play music" in command:
        play_music()
        
    elif "schedule task" in command:
        schedule_task()
        
    # Add more command-specific logic here