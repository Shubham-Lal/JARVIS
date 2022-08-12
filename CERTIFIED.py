import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg

#image = mpimg.imread('certified.png')

# Voice Pack by Microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



# Audio Input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



# Starting Intro 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hii ! Good Morning!")
    elif hour>=12 and hour<18:
        speak("Hii ! Good Afternoon!")
    elif hour>=18 and hour<21:
        speak("Hii ! Good Evening!")
    elif hour>=21 and hour<24:
        speak("Hii ! Good Night!")

    speak("I am CERTIFIED, Hope your day is great")


# Taking Voice Input from user
def takeCommand():
    
    # Microphone On
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                # Seconds of non-speaking audio before a phrase is considered complete
        #r.energy_threshold = 1000              
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# Email Address and Password
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('presidentofmyhouse.new@gmail.com', 'kumkumlal')
    server.sendmail('shubhamlal.new@gmail.com', to, content)
    server.close()


# Executing
if __name__ == "__main__":
    #plt.imshow(image)
    #plt.show()
    wishMe()
    while True:
    
        query = takeCommand().lower()

    # LOgic for executing tasks based on query
        
        # Searchs on Wikipedia
        if 'in wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search' in query:
            a = query.split()
            b = a[1]
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            url = (b+".com")         
            speak(f"Searching {b} on Chrome " )
            webbrowser.get(chrome_path).open(url)
        
        # Opens Youtube
        #elif 'open youtube' in query:
            #speak("Opening Youtube for you")
            #webbrowser.open("youtube.com")

        # Opens Google
        #elif 'google' in query:
            #speak("Opening Google for you")
            #webbrowser.open("google.com")
            
        # Plays Music
        elif 'play music' in query:
            music_dir = ''
            songs = os.liostdir(music_dr)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # Current Time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        # Opens Visual Studio Code
        elif 'open visual studio code' in query:
            vscpath = "C:\\Users\\Shubham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code for you")
            os.startfile(vscpath)

        # Emails
        elif 'send email' in query:
            try:
                speak("What's the message?")
                content = takeCommand()
                to = "shubhamlal.new@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to this Email at the moment. Sorry for the inconvenience.")

        elif 'terminate' in query:
            quit()




        
        


        




