''' Developed by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Python-Mini-Projects '''

import webbrowser
import random, os
import speech_recognition as sr
from time import sleep
from selenium import webdriver
import wikipedia
from time import strftime
import time, sys
import datetime
from PIL import ImageGrab
import subprocess
import requests

def talktome(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

r = sr.Recognizer()
booting = ['Your Friend Eric, The Robo has begun', 'Eric Assistant at your service',
           'Currently starting Eric Virtual Assistant']
greetings = ["hello", "hello there", "Hi, I am Eric", "Greetings human", "Your wish is my command",
             "Hello user", "Hello user, what would you like to do?"]
userGreet = ["hello", "hi", "start", "hey"]
closing = ['Shutting down', 'Closing Eric\'s brain Assistant', 'Have a nice day','Eric is signing off', 'signing off']
whoareyou = ['who are you', 'what is your name','name','Describe yourself','Tell me about yourself']
musical = ["What are we watching today", "Are gonna to sing some karaoke", "Listening to some music today",
           "Good thing I have my dancing module in", "I use to listen pahchaan music playlist"]
talktome(random.choice(booting))


def greeting(data):
    talktome(random.choice(greetings))
    main()


def whatsup():
    talktome('Just doing my thing')


def search(data):
    driver = webdriver.Chrome()
    driver.get("http://google.com/search?q=" + data.split("search", 1)[1])
    wordSearch = data.split("search", 1)[1]
    sentence = wikipedia.summary(wordSearch, sentences=4)
    talktome(sentence)
    main()


def youtube(data):
    talktome(random.choice(musical))
    webbrowser.open("http://youtube.com")
    sleep(2)
    main()


def time(data):
    current = strftime("%I:%M")
    talktome("The current time is " + current)
    main()


def tDate(date):
    day = strftime("%d")
    month = strftime("%B")
    talktome("Todays date is " + day + " " + month)
    main()


def Gmail(data):
    talktome("Opening Email Client")
    webbrowser.open("http://gmail.com")
    main()


def Amazon(data):
    talktome("Opening Amazon to purchase " + data.split('buy', 1)[1])
    webbrowser.open("https://www.amazon.com/s/field-keywords=", data.split('buy', 1)[1])
    main()


def SS():
    talktome("Taking screenshot")
    name = random.randint(1000, 300000)
    time.sleep(5)
    ImageGrab.grab().save("screenshot" + str(name), "JPEG")
    talktome("Screenshot saved at " + name)
    print("Screenshot saved at" + name)
    main()


def intro():
    msg = "I am Eric and i am invented by Shubham Agarwal"
    talktome(msg)


def calculate(data):
    if 'plus' in data:
        str.replace("plus", "+")

    value1, value2 = (data.split('calculate', 1)[1])
    answer = value1 + value2
    talktome("The answer to that is " + answer)


def locate(data):
    place = data.split('locate', 1)[1]
    talktome("Locating " + place)
    webbrowser.open("https://www.google.ca/maps/place/" + place + "/")
    main()



def main():
    with sr.Microphone() as source:
        print("Say something then wait.")
        audio = r.listen(source)

    try:
        data = r.recognize_google(audio)
        print("You said:" + data)
        if data == 'hello':
            greeting(data)
        if 'search' in data:
            talktome("Opening web browser to search for " + data.split("search", 1)[1])
            search(data)
        if 'YouTube' in data:
            youtube(data)
        if 'time' in data:
            time(data)
        if 'date' in data:
            tDate(data)
        if 'whats up' in data:
            whatsup()
        if data == 'shut down':
            talktome(random.choice(closing))
            sys.exit()
        if 'thank you' in data:
            talktome("You are welcome")
        if data == 'Eric':
            talktome("Yes, I am here")
        if data == 'email':
            Gmail(data)
        if 'buy' in data:
            Amazon(data)
        if data in whoareyou:
            intro()
        if data == 'screenshot':
            SS()
        if 'calculate' in data:
            calculate(data)
        if 'locate' in data:
            locate(data)
        if data == 'Notepad':
            talktome("Opening notepad")
            subprocess.call(['notepad.exe'])
            main()

        else:
            main()



    except sr.UnknownValueError:
        talktome("Google Speech Recognition could not understand what you were trying to say")
        main()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recoginition Service;{0}".format(e))
        main()


main()
