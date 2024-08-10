# Project Description: create a voice assistant using pyttex3 and speech recognition
# Write code only

pip install pyttsx3 speech_recognition
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    """Listen for user input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

def speak(text):
    """Convert the given text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet():
    """Greet the user."""
    speak("Hello, how can I assist you today?")

def main():
    """The main loop of the voice assistant."""
    while True:
        query = listen()
        if 'exit' in query or 'bye' in query:
            speak("Goodbye, have a great day!")
            break
        # Add more functionality here by checking for different queries
        greet()

if __name__ == "__main__":
    main()
python voice_assistant.py