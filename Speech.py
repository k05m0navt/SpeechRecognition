import speech_recognition as sr

text = ""

r = sr.Recognizer()
while (text != "Выход"):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ru-RU", key = "151deb9067398d06d646efdad6271c7892d39818")
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
