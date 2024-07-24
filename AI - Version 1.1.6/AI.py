import pyttsx3 # Imported for Speak function
import datetime # Imported for Date and Time Function
import speech_recognition as sr #imported for speech recognition
import wikipedia # for browsing functions
import smtplib #for email function
import webbrowser as wb
import psutil #for cpu information
import pyjokes #for jokes function
import os
import ctypes
import pyautogui
from ecapture import ecapture as ec
import random
import winshell
import json
import requests
import wolframalpha
from urllib.request import urlopen
import time
import shutil
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred)
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
    #date_()
    #time_()
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

    speak("Tilak is at your service.")


def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
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

def username():
    speak("What should i call you sir")
    uname = TakeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("Please tell me how can I help you today ")

if __name__ == "__main__":
    while True:
        print("Hi buddy You Want To create Account Or Login")
        speak("Hi buddy You Want To create Account Or Login")
        ok = TakeCommand().lower()
        
        if 'create account' in ok:
            speak("Please inter your email Address")
            email = input('Please inter your email Address : ')
            speak("Please inter your password")
            password = input('Please inter your password : ')
            speak("Please create your ID")
            id = input('Please create your ID : ')
            speak("Please inter your phone number with country code")
            phone = input('Please inter your phone number with country code : ')
            user = auth.create_user(uid = id , email = email , password = password , phone_number = phone)
            print("creating....")
            speak("creating")
            print("user created successfully : {0}".format(user.uid))
            speak("user created successfully")

        elif 'login' in ok:
            speak("Please inter your email Address")
            email = input('Please inter your email Address : ')
            speak("Please inter your ID")
            id = input('Please inter your ID : ')
            user = auth.get_user_by_email(email)
            if email == user.email and id == user.uid:
                print("loged in")
                wishme()
                username()
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

                    elif 'powerpoint' in query:
                        speak('Openning power point presentation......')
                        power_point = r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE'
                        os.startfile(power_point)

                    elif 'excel' in query:
                        speak('Openning Excel......')
                        excel = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'
                        os.startfile(excel)

                    elif 'edge' in query:
                        speak('Openning Edge Browser......')
                        edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
                        os.startfile(edge)

                    elif 'notepad' in query:
                        speak('Openning notepad ++......')
                        notepad = r'C:\Program Files (x86)\Notepad++\notepad++.exe'
                        os.startfile(notepad)

                    elif 'python' in query:
                        speak('Openning python shell......')
                        idle = r'E:\vs code\python.exe'
                        os.startfile(idle)

                    elif 'library' in query:
                        speak('Openning libre office......')
                        libre = r'C:\Program Files\LibreOffice\program\soffice.exe'
                        os.startfile(libre)

                    elif 'fdm' in query or 'free download manager' in query:
                        speak('Openning fdm......')
                        fdm = r'C:\Program Files\Softdeluxe\Free Download Manager\fdm.exe'
                        os.startfile(fdm)

                    elif 'outlook' in query:
                        speak('Openning outlook......')
                        outlook = r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE'
                        os.startfile(outlook)

                    elif 'android studio' in query:
                        speak('Openning android studio.......')
                        android = r'E:\andriod +++++\bin\studio64.exe'
                        os.startfile(android)

                    elif 'vs code' in query:
                        speak('Openning vs code......')
                        vs_code = r'C:\Users\pavan\AppData\Local\Programs\Microsoft VS Code\Code.exe'
                        os.startfile(vs_code)

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
                    elif 'lock window' in query:
                            speak("locking the device")
                            ctypes.windll.user32.LockWorkStation()
                    elif 'empty recycle bin' in query:
                        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                        speak("Recycle Bin Recycled")

                    elif 'about' in query or 'who are you' in query:
                        print('I Am Vertual Assistent of Pavan Singh Version 1.1.2 And My name is tilak')
                        speak('I Am Vertual Assistent of Pavan Singh Version 1.1.2 And My name is tilak')

                    elif 'how are you' in query:
                        speak("I am fine, Thank you")
                        speak("How are you, Sir")

                    elif 'fine' in query or "good" in query:
                        speak("It's good to know that your fine")

                    elif "who made you" in query or "who created you" in query:
                        speak("I have been created by Pavan Singh.")

                    elif "who i am" in query:
                        speak("If you talk then definitely your human.")

                    elif 'change background' in query:
                        ctypes.windll.user32.SystemParametersInfoW(20,0,"D:\project - 4 ( AI Assistent )\AI - Version 1.1.2\background.jpg",0)
                        speak("Background changed successfully")

                    elif "why you came to world" in query:
                        speak("Thanks to Pavan singh. further It's a secret")
                    
                    elif "camera" in query or "take a photo" in query:
                        ec.capture(0, "Tilak Camera ", "img.jpg")

                    elif "will you be my gf" in query or "will you be my bf" in query:  
                        speak("I'm not sure about, may be you should give me some time")
             
                    elif "i love you" in query:
                        speak("It's hard to understand")

                    elif 'jay shri ram' in query:
                        speak('jay shri ram')

            
            else:
                print("Something Went Wrong , please check your login credential or internet connectivity")
                speak("Something Went Wrong , please check your login credential or internet connectivity")

        elif 'go offline' in ok:
                        print('Going to Offline , Have a nice day ')
                        speak('Going Offline sir , Have a nice day ')
                        quit()

