import subprocess
import sys
import wolframalpha
import pyttsx3
import tkinter
import cv2
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pywhatkit as kit
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
from requests import get
import pyautogui
import shutil
from twilio.rest import Client
#from client.textui import progress
from ecapture import ecapture as ec
from b4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id);
engine.setProperty('voices',voices[0].id)

#text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    #r.adjust_for_ambient_noise()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.record(source,duration=2.5)
        #audio = r.listen(source,timeout=1,phrase_time_limit=5)
    #text = r.recognize_google_cloud(audio)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        print("Say that again please")
        return "none"
    return query

def wish():
    hour = datetime.datetime.now().hour
    if (hour >= 6 ) and (hour < 12):
        speak(f"Good Morning sir!")
    elif (hour >=12 ) and (hour < 16) :
        speak(f"Good Afternoon sir!")
    elif (hour >= 16) and (hour < 20):
        speak(f"Good Evening sir!")
    elif (hour >= 21) and (hour <6):
        speak(f"Good Night sir!")
    else:
        speak(f"Have a good day sir!")
#Introduction of A.I
    speak(f"I am DAVID.")


def username():
    speak("What should i call you sir")
    uname = takecommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")
if __name__ == "__main__":
    wish()

    #username()
# Commands to open Applications
    while True:
    #if 1:
        query = takecommand().lower()
    #logic building module
        if "open notepad" in query:
            path = "C:\\Windows\\Notepad.exe"
            os.startfile(path)
        #about the AI
        elif "david means" in query or "meaning of david" in query:
            speak("the meaning of DAVID is Dynamic Artificial Virtual Intelligence Device")
            speak("Description: DAVID is a highly adaptable AI system designed to handle a wide range of tasks with efficiency and precision.")

        #elif "about AI" or "about DAVID AI" or "about DAVID" in query:
         #   speak("the meaning of DAVID is Dynamic Artificial Virtual Intelligence Device")
          # google
        # speak("Description: DAVID is a highly adaptable AI system designed to handle a wide range of tasks with efficiency and precision.")


        elif "open adobe reader" in query:
            path = "C:\\Users\\Public\\Desktop\\Acrobat Reader.lnk"
            os.startfile(path)

        elif "open chrome" in query:
            speak("what should I search sir?")
            path="C:\\Program Files\\Google\\Chrome\\Application\\Chrome"
            os.startfile(path)
            cm = takecommand().lower()
            pyautogui.typewrite(f"{cm}")
            pyautogui.sleep(2)
            pyautogui.press("enter")


        elif "open vs" in query:
            path ="C:\\Users\\Acer\\Desktop\\Visual Studio Code.lnk"
            os.startfile(path)

        elif "shut down" in query:
            path = "C:\\Windows\\System32\\SlideToShutDown.exe"
            os.startfile(path)

        elif "open" in query:
            query = query.replace("open","")
            query = query.replace("David","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "open xampp" in query:
            path = "C:\\Users\\Acer\\Desktop\\XAMPP Control Panel.lnk"
            os.startfile(path)


        elif "play music" in query:

            # Initialize the WebDriver
            #driver = webdriver.Edge()  # or webdriver.Firefox() for Firefox

            #def play_music_on_wynk():
                # Open Wynk Music website
                webbrowser.open("https://wynk.in/music")

                # Wait for the page to load
                time.sleep(5)

                # Find the search bar and enter the song name
                #search_bar = WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search for Songs, Albums, Artists..."]')))
                #speak("which Song should I play sir...?")
                #cm = takecommand().lower()
                #search_bar.send_keys(f'{cm}')
                #search_bar.send_keys(Keys.RETURN)

                # Wait for search results to load
               # time.sleep(5)

                # Click on the first search result
                #first_result = webdriver.find_element(By.XPATH,'//div[@class="song-card"]')
                #first_result.click()

                #speak(f"Playing {cm} on Wynk Music")
                #play_music_on_wynk("Your Song Name Here")


        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            speak("Which information you want sir..??")
            cm=takecommand().lower()
            results = wikipedia.summary(query, sentences = 3)
            webbrowser.open("https://wikipedia.org")
            speak("According to Wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("what should I search on Google\n")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open stackoverflow" in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif "whats the time" in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "search" in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "news" in query:

            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))



        elif "IP Address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")

        elif "send message" in query:
            kit.sendwhatmsg("+919028228659","this is testing of advance david ai",5,1)

        elif "play songs on youtube" in query:
            speak("which song would you like to listen...?")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

#to end/stop the david ai
        elif "exit" in query:
            speak("Thanks for giving me your time")
            exit()

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop david from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "no thanks " in query:
            speak("thanks for using me sir","have a nice day")
            exit()

# Commands to Close opend Applications
        elif "close" in query:
            speak("Which Application should I close sir...?")
            query = query.replace("close","")
            query = query.replace("David","")
            cm = takecommand().lower()
            speak("CLosing " f"{cm}")
            pyautogui.typewrite(f"{cm}")
            pyautogui.sleep(2)
            pyautogui.hotkey('alt','f4')
            pyautogui.press("enter")

#to switch application and some automation
        elif "switch application" in query:
            speak("Which Application should I switch sir...?")
            query = query.replace("switch application", "")
            query = query.replace("David", "")
            cm = takecommand().lower()
            speak("Switching " f"{cm}")
            pyautogui.hotkey('alt','tab')
            pyautogui.press("enter")

#to minimize the active window
        elif "minimize" in query:
            pyautogui.hotkey('win','m')

        elif "mini" in query:
            query = query.replace("mini", "")
            query = query.replace("David", "")
            speak("to which side to minimize the window sir..?")
            cm = takecommand().lower()
            speak("Minimizing the window " f"{cm}")
            pyautogui.hotkey("win", f"{cm}")

        elif "scroll" in query:
            speak("to which side sir?")
            cm = takecommand().lower()
            pyautogui.scroll(f'{cm}')


        # speak("do you have any either work to do, let me know...")
