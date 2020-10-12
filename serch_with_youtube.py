import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)

r = sr.Recognizer()

r.energy_threshold =500

with sr.Microphone()as source:
    print("Speak !!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said :".format(text))
        url='https://www.youtube.com/results?search_query='
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("Can't Recognize !!!")

