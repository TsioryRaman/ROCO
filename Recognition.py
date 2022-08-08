import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()


def recognition():
    with mic as source:
        print("ici")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        print("...")

        return r.recognize_google(audio, language='fr-FR')
