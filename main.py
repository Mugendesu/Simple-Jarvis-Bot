import speech_recognition as sr
import webbrowser
import pyttsx3
import playSong

recognizer = sr.Recognizer()

microphone = sr.Microphone()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def process_text(text):
    if "open" in text:
        url = (text.split("open")[1])
        speak(f"Opening {url}")
        webbrowser.open((f"www.{url}.com").replace(' ',""))
    elif "search" in text:
        url=(text.split("search")[1]).split(" ") 
        speak(f"Searching for {' '.join(url)}")
        webbrowser.open((f"https://www.google.com/search?q={'%20'.join(url)}"))
    elif "play" in text:
        song = (text.split("play")[1]).split(" ")
        link = playSong.music[(' '.join(song[1:])).lower()]
        speak(f"Playing {song}")
        webbrowser.open(link)
    elif "deactivate" in text:
        speak("Deactivating Jarvis")
        exit()
    else:
        raise Exception("Invalid command")




if __name__ == '__main__':
    speak("Initialising Jarvis.....")
    with microphone as source:
        # recognizer.adjust_for_ambient_noise(source)
        # recognizer.pause_threshold = 1
        print("Listening....")
        speak("Say Jarvis to activate me")
        while True:
            try:
                audio1 = recognizer.listen(source)

                text = recognizer.recognize_google(audio1)
                if "Jarvis" in text:
                    speak("How can I help you?")
        
                    audio = recognizer.listen(source,phrase_time_limit=5)
                    print("Recognizing....")
                    try:
                        text = recognizer.recognize_google(audio)
                        print("You said: ", text)
                        # speak("You said: " + text)
                        process_text(text)
                    except Exception as e:
                        print("Error: ", e)
                        speak("Sorry, I didn't get that.")
            except Exception as e:
                pass

                