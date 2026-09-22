import speech_recognition as sr
import pyttsx3
import datetime
import zenithConfig
import searchHandler as srch
import openHandler as opn
import notifyHandler as ntfy
## Zenith Assistant
## Created by Team Orbi | 2026

def talk(text):
    print(f"Zenith: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Error with pyttsx3, have you installed it?")

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        talk("Good Morning " + zenithConfig.userName +", how may I help you?")
    elif hour < 18:
        talk("Good Afternoon " + zenithConfig.userName +", how may I help you?")
    else:
        talk("Good Evening "+ zenithConfig.userName +", how may I help you?")

def textInput():
    return input("User: ").lower()

def zenithCommands(query):
    if 'time' in query:
        talk('The current time is ' + datetime.datetime.now().strftime("%I:%M %p"))
    elif 'search' in query:
        query = query.replace("search", "")
        talk(srch.sortSearch(query))
    elif 'open' in query:
        query = query.replace("open", "")
        talk(opn.openSort(query))
    elif 'notify' in query:
        query = query.replace("notify", "")
        talk(ntfy.notifySort(query))
    elif 'exit' in query:
        exit()
    else:
        talk('Sorry, I dont recognize that command')


def bootZenith():
    global query
    greet_user()
    while True:
        if zenithConfig.inputMethod == 'text':
            query = textInput()
            zenithCommands(query)
        else:
            print('Input method not supported')


bootZenith()