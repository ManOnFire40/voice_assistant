import speech_recognition as sr
import pyttsx3
import os
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth


r = sr.Recognizer()
engine = pyttsx3.init()
scope = "user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def say_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak("The current time is " + current_time)


def shutdown_computer():
    speak("Shutting down the computer")
    os.system("shutdown /s /t 1")

def pause_music():
    sp.pause_playback()
    speak("Music paused")

def play_music():
    sp.start_playback()
    speak("Music resumed")
def handle_command(command):
    if "time" in command:
        say_time()
    elif "shutdown" in command:
        shutdown_computer()
    elif "pause music" in command:
        pause_music()
    elif "play music" in command:
        play_music()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("Command:", command)
            handle_command(command)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Sorry, I couldn't request results from the speech recognition service. {0}".format(e))

        main()  # Recursive call to keep listening for commands

main()  # Start the virtual assistant
