import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine= pyttsx3.init()
newapi = '39d7b16aac9342199962c0623318794f'

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):

    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load("temp.mp3")  # Replace with the path to your MP3 file

# Play the MP3 file
    pygame.mixer.music.play()

# Keep the program running while the music plays
    while pygame.mixer.music.get_busy():  # Check if the music is still playing
        pygame.time.Clock().tick(10)  # You can adjust the tick rate as needed
    pygame.mixer.music.unload()
    os.remove('temp.mp3')



def aiProcess(command):
    client = OpenAI(
        api_key="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",
    )
    completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. GIve short responses please"},
                {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

    

def processCommand(command):
    command = command.lower()
    if 'open google' in command:
        webbrowser.open('https://google.com')
    elif 'open facebook' in command:
        webbrowser.open('https://facebook.com')
    elif 'open youtube' in command:
        webbrowser.open('https://youtube.com')
    elif 'open linkedin' in command:
        webbrowser.open('https://linkedin.com')
    elif command.startswith('play'):
        song = command.split(' ')[1]

        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif 'news' in command:
        r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=39d7b16aac9342199962c0623318794f')
        if r.status_code == 200:
            

            data = r.json()  # Convert the response to JSON
            articles = data.get('articles', []) 
             # Extract articles (headlines)
            for article in articles:
                speak(article['title']) 
    
    else:
        # Let openAI handle the request
        output=aiprocess(c)
        speak(output)
         
           



        





if __name__ == '__main__':
    speak('Initializing Jarvis....')
    # Listen for the wake word 'Jarvis'
    while True:
        r = sr.Recognizer()
        print('recognizing..')
        try:

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening!")
                audio = r.listen(source, timeout =5,phrase_time_limit =1)
            word = r.recognize_google(audio).lower()
            if(word.lower() == 'jarvis'):
                speak('Ya')
                with sr.Microphone() as source:
                    print("Jarvis Active!")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command= r.recognize_google(audio).lower()

                    processCommand(command)
            else:
                print('listening for jarvis')        



            

        except Exception as e:
            print("error; {0}".format(e))


 


