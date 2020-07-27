from speakText import SpeakText
from listenVoice import ListenVoice

speakText = SpeakText()
listenVoice = ListenVoice()

speakText.speak("hello sir")

said = ""
while said != "exit":
    said = listenVoice.listen()    

    if(said == "Jarvis"):
        speakText.speak("yes sir")
    elif(said == "exit"):
        speakText.speak("goodbye sir")
    else:
        speakText.speak("couldn't understand")