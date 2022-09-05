import speech_recognition as sr
r = sr.Recognizer()

mic = sr.Microphone()


def recognition():
    with mic as source:
        print("En train d'ecouter...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        print("reconaissance en cours ...")

        return r.recognize_google(audio, language='fr-FR')
