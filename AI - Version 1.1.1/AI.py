import pyttsx3 # Imported for Speak function
import datetime # Imported for Date and Time Function
import speech_recognition as sr #imported for speech recognition
import wikipedia # for browsing functions
import smtplib #for email function
import webbrowser as wb
import psutil #for cpu information
import pyjokes #for jokes function
import os
import pyautogui
import random
import json
import requests
import wolframalpha
from urllib.request import urlopen
import time



engine = pyttsx3.init()
wolframalpha_app_id = 'H79VET-VJA6G3LUR5'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #And ("%H:%M:%S") for 24 hour format
    speak("The Current Time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Jai Shree Ram ! Welcome Back Prime !")
    date_()
    time_()
    #Below is Code For Greetings
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir! ")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir! ")
    else:
        speak("Good Night Sir !")

    speak("I am at your service. Please tell me how can I help you today ")


def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function, you must enable low security
    server.login("ucempavan@gmail.com" , 'pawansinghprime555' )
    server.sendmail('ucempavan@gmail.com' , to, content )
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/pavan/Desktop/screenshot.png')
    
def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at '+usage)
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    print('Battery is at')
    print(battery.percent)
    speak('Battery is at')
    speak(battery.percent)
    speak('Percent')

def joke():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()

    while True:
        query = TakeCommand().lower()
        if 'time' in query: #tells time whenever asked for
            time_()
        elif 'date' in query: #tells date whenever asked for
            date_()
        elif 'wikipedia' in query:
            print("Searching...")
            speak("Searching...")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('Accornding to Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should i say")
                content=TakeCommand()
                #provide reciever email address
                speak("who is the reciever?")
                reciever=input("Enter Reciever's Email : ")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak( 'Email has been sent.')

            except Exception as e:
                print(e)
                speak("Unab1e to send Email." )

        elif 'search in chrome' in query:
            speak('What should i Search ?')
            chromepath = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #opens only .com sites
            
        elif 'search youtube' in query:
            speak('what should I search?')
            search_Term = TakeCommand().lower()
            speak("Here We go to YOUTUBE !")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak('Searching.....')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            print('Going to Offline , Have a nice day ')
            speak('Going Offline sir , Have a nice day ')
            quit()

        elif 'word' in query:
            speak('Openning ms word......')
            ms_word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should i write , sir ?")
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak('Should i include date and time ?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes , sir!')
            else:
                file.write(notes)
                speak('Done sir!')

        elif 'show note' in query:
            speak('Showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'E:/songs'
            music = os.listdir(songs_dir)
            speak('what should i play ?')
            speak('select a number...')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you . please try Again.')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,10)
            os.startfile(os.path.join(songs_dir,music[no]))
            
            
        elif 'remember that' in query:
            speak("what should i remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remember that'+remember.read())


        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            
        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=a9045b4da2724ab78b4cabb84e32d565")
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top headlines from the Business Industry')
                print('==========TOP HEADLINES=========='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
            except Exception as e:
                print(str(e))
                    
        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('the Answer is : '+answer)
            speak('the answer is'+answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")

        elif 'stop listening' in query:
            speak('For how many second you want me to stop listening to your commands?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
