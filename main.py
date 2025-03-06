# Imorting required libraries
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import dict_lib
import model_api

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
    if "start" in text:
        app = (text.split("start")[1]).split(" ")
        app1 = dict_lib.open_applications[(' '.join(app[1:-1])).lower()] 
        speak(f"Opening {app[1:-1]}")
        os.startfile(app1)
        
    # For closing applications
    if "close" in text:
        app = (text.split("close")[1]).split(" ")
        app1 = dict_lib.close_applications[(' '.join(app[1:])).lower()] 
        speak(f"Closing {app}")
        os.system(f'taskkill /f /im {app1}')
        
    # For opening websites
    elif "open" in text:
        urls = (text.split("open")[1]).split(" ")
        # url = dict_lib.websites["".join(urls[1:])] <--- Uncomment this line and Comment the line below to use this using dictionary
        url = model_api.bot_init(f"What is the Link for {''.join(urls[1:])} Website? Don't say anything else just give the link. If you cant find the website , give the link of the closest match.")
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
        # link = dict_lib.music[(' '.join(song[1:])).lower()] <--- Uncomment this line and Comment the line below to use this using dictionary
        link = model_api.bot_init(f"What is link for the youtube song '{' '.join(song[1:])}'? , don't say anything else just give the link. If you cant find the song , give the link of the closest match. Also give direct link of the video not a search link")
        # deep_seek.chat_log.pop()
        speak(f"Playing {song}")
        webbrowser.open(link)   
        
    # For deactivating Jarvis   
    elif "deactivate" in text:
        speak("Deactivating Jarvis")
        exit()
        
    # For commands other then those described above
    else:
        reply = model_api.bot_init(f"{text}. Don't add any special characters like * , # , etc.. Reply only in alphanumerical text.")
        speak(reply)


# Main function
if __name__ == '__main__':
    speak("Initialising Jarvis.....")
    print("Listening...." , flush=True)
    speak("Say Jarvis to activate me")
    while True:
        with sr.Microphone() as source:
            # recognizer.adjust_for_ambient_noise(source)
            # recognizer.pause_threshold = 1
            try:
                audio1 = recognizer.listen(source) 

                text = recognizer.recognize_google(audio1) 
                if "Jarvis" in text:
                    speak("How can I help you?")
        
                    audio = recognizer.listen(source,phrase_time_limit=10) 
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

                
