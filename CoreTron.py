import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import wolframalpha
import pyfirmata
import turtle





board = pyfirmata.Arduino('/dev/ttyACM0')

try:
    app = wolframalpha.Client("UG5AG6-YW36RTPH68")
except Exception:
    print("Internet Error!!!")

#Text To Speech

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')
engine.setProperty('volume', 1)
#print(voices)
engine.setProperty('voice',voices[13].id)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning i am virtual assistant jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon i am virtual assistant jarvis") 
    else:
        speak("good night i am virtual assistant jarvis")  

#now convert audio to text
# 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.:")
        audio = r.listen(source)
    try:
        print("Recognising..:") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("error...")
        print("error") 
        return "none"
    return text

#for main function                               
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()
        if "switch on" in query:
            board.digital[7].write(1)
            print("Turned on")
            speak("Lights are turned on ...")
        elif "switch off" in query:
            board.digital[7].write(0)
            print("Turned off")
            speak("Lights are turned off ...")
        elif "jarvis" in query:
            chatbot = ChatBot("AI-Chat")
            #trainer = ChatterBotCorpusTrainer(chatbot)
            #trainer.train('chatterbot.corpus.english')
            
            e = chatbot.get_response(query)
            speak(e)
            print(e)
        elif "search" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif "show" in query:
            d_url="https://duckduckgo.com/?q="+query
            speak("Seaching Please Wait...")
            webbrowser.open(d_url)
            
        elif "birthday" in query:
            print("Happy Birthday to you !")
            board.digital[7].write(1)
            speak("Happy Birthday to you, Happy Birthday to you, Happy Birthday dear kaader maamoojaan, Happy Birthday to you !")
            board.digital[7].write(0)
        	

        elif "audio" in query:
            print("Opening Audio Settings...")
            speak("Opening audio Settings Please Wait.")

        elif "work" in query:
            print("Opening Your Work...")
            speak("Opening Work")
            os.system('libreoffice')

        elif 'class' in query:
            print("Opening class")
            speak("Opening class Please Wait")
            webbrowser.open("classroom.google.com/u/0/h")
            
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com") 
            speak("opening snapdeal")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")   
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(video_dir)
            os.system('rhythmbox')  
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown now')
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I program how can i help you chat withh me run programs or search internet with me ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query:
            hel = "Hello Sire ! How May i Help you.."
            print(hel)
            speak(hel)
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()    
        else:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Error!!!")
                
                    
                            
