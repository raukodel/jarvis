import speech_recognition as sr

class ListenVoice():

    def __init__(self):
        super().__init__()

    def listen(self):
        said = ""

        try :
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""

                said = r.recognize_google(audio)
                print(said)
        except Exception as e:
            print("Exception: listen")
            said = ""
                    
        return said