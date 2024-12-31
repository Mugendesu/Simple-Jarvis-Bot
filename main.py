# Imorting required libraries
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import dict_lib

# Initialising the speech recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# Function to process the text    
def text_processing(text):
    # For opening applications
    if "open" and ("app" or "application") in text:
        app = (text.split("open")[1]).split(" ")
        app1 = dict_lib.open_applications[(' '.join(app[1:-1])).lower()] 
        speak(f"Opening {app[1:-1]}")
        os.startfile(app1)
    # For closing applications
    elif "close" in text:
        app = (text.split("close")[1]).split(" ")
        app1 = dict_lib.close_applications[(' '.join(app[1:])).lower()] 
        speak(f"Closing {app}")
        os.system(f'taskkill /f /im {app1}')
    # For opening websites
    elif "open" in text:
        urls = (text.split("open")[1]).split(" ")
        url = dict_lib.websites["".join(urls[1:])] 
        speak(f"Opening {' '.join(urls)}")
        webbrowser.open(url)
    # For searching on google
    elif "search" in text:
        url=(text.split("search")[1]).split(" ") 
        speak(f"Searching for {' '.join(url)}")
        webbrowser.open((f"https://www.google.com/search?q={'%20'.join(url)}"))
    # For playing songs
    elif "play" in text:
        song = (text.split("play")[1]).split(" ")
        link = dict_lib.music[(' '.join(song[1:])).lower()]
        speak(f"Playing {song}")
        webbrowser.open(link)   
    # For deactivating Jarvis   
    elif "deactivate" in text:
        speak("Deactivating Jarvis")
        exit()
    # For invalid commands
    else:
        raise Exception("Invalid command")

# Main function
if __name__ == '__main__':
    speak("Initialising Jarvis.....")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        # recognizer.pause_threshold = 1
        print("Listening...." , flush=True)
        speak("Say Jarvis to activate me")
        while True:
            try:
                audio1 = recognizer.listen(source) 

                text = recognizer.recognize_google(audio1) 
                if "Jarvis" in text:
                    speak("How can I help you?")
        
                    audio = recognizer.listen(source,phrase_time_limit=5) 
                    print("Recognizing....", flush=True)    
                    try:
                        text = recognizer.recognize_google(audio) 
                        print("You said: ", text, flush=True)
                        # speak("You said: " + text)
                        text_processing((text).lower())
                    except Exception as e:
                        print("Error: ", e)
                        speak("Sorry, I didn't get that. ")
                        
            except Exception as e:
                pass

                
