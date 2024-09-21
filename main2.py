import speech_recognition as sr
import webbrowser 
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
#pip install pocketsphinxs
recognizer = sr .Recognizer()
engine = pyttsx3.init()
newsapi = "d3a099b448104dcabdb60134e8296a4e"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
     tts = gTTS(text)
     tts.save('temp.mp3')
     
# Initialize the mixer
     pygame.mixer.init()

# Load your MP3 file
     pygame.mixer.music.load('yourfile.mp3')

# Play the MP3 file
     pygame.mixer.music.play()

# Keep the script running until the music stops
     while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)

     pygame.mixer.music.unload()
     os.remove("temp.mp3")


def aiprocess(command):
    client = OpenAI(api_key= "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",
)
    completion =client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud.give short responce please"}, 
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the Json responce
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            #print the headline
            for article in articles:
                speak(article['title'])
    else:
        #Let OpenAI handle the request
        output=aiprocess(c)
        speak (output)

if __name__=="__main__":
     speak("Initializing Jarvis....")
     while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
