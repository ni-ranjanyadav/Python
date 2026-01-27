import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration = 1)
        audio = recognizer.listen(source)
    return audio
if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Say somthing")
                recognizer.adjust_for_ambient_noise(source, duration = 1)
                audio = recognizer.listen(source)
            
            command = recognizer.recognize_google(audio)
            print("You said: ", command)
        
            if "jarvis" in command.lower():
                speak("Yes, how can I help you")
                
            elif "open google" in command.lower():
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
                    
            elif "open youtube" in command.lower():
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com")
                break
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Network error:", e)
