from gtts import gTTS
import pygame

class SpeakText():

    def __init__(self):
        super().__init__()

    def speak(self, text):
        try:
            tts = gTTS(text=text, lang="en")
            filename = "voice.mp3"
            tts.save(filename)

            pygame.mixer.init()
            pygame.display.set_mode((1,1))
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        except Exception as e:
            print("Exception: " + e)