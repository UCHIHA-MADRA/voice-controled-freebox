import speech_recognition as sr
import requests

# Set language to English
r = sr.Recognizer()
r.energy_threshold = 300

while True:
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            s = r.recognize_google(audio, language="en-US")
            print("You said " + s)
            if s.lower() == "freebox":
                print("POWER")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=power')
            elif s.lower() == "ok":
                print("OK")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=ok')
            elif s.lower() == "menu":
                print("MENU")
                requests.get('http://hd1.freebox.fr/pub/remote_control?code=34679945&key=home')
            elif s.isdigit():
                print(s)
                requests.get(f'http://hd1.freebox.fr/pub/remote_control?code=34679945&key={s}') 
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
