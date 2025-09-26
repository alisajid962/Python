import speech_recognition as sr
import pyttsx3
import requests
import datetime
import subprocess
import platform

# Initialize TTS
tts = pyttsx3.init()
def speak(text):
    print("Jarvis:", text)  # also show in console
    tts.say(text)
    tts.runAndWait()

# Initialize STT
recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen(timeout=5, phrase_time_limit=8):
    with mic as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("STT error:", e)
        return ""

# Simple Wikipedia search using MediaWiki API
def wiki_summary(query):
    
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + requests.utils.requote_uri(query)
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data.get("extract")
        else:
            return None
    except Exception as e:
        print("Wiki request failed:", e)
        return None

# Command handler with keyword matching
def handle_command(text):
    if not text:
        speak("I didn't catch that.")
        return

    # Time command
    if "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    # Open Notepad
    elif "open notepad" in text or "notepad" in text:
        if platform.system() == "Windows":
            subprocess.Popen(["notepad.exe"])
            speak("Opening Notepad")
        else:
            speak("This command works only on Windows right now.")

    # Wikipedia search
    elif "wikipedia" in text or "search" in text:
        q = text.replace("search wikipedia about", "").replace("search", "").replace("wikipedia", "").strip()
        if not q:
            speak("Please say what you want me to search on Wikipedia.")
        else:
            speak(f"Searching Wikipedia for {q}")
            summary = wiki_summary(q)
            if summary:
                speak(summary)
            else:
                speak("Sorry, I couldn't find that.")

    else:
        speak("Sorry, I don't know that command yet.")

# Main loop
if __name__ == "__main__":
    speak("Jarvis mini is ready. Press Enter to give a command.")
    while True:
        input("Press Enter to speak (or Ctrl+C to exit)...")
        txt = listen()
        handle_command(txt)
