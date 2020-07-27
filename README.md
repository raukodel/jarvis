# jarvis
I made this project to test speech recognition and make some fun things. 

# Python 3
Enviroment
```
$ pip3 install virtualenv
$ virtualenv name_of_env
$ source env/bin/activate
```
Install dependencies
```
$ pip3 install speechrecognition
$ pip3 install gTTS
```

# For pyaudio
```
$ sudo apt-get install python3-pyaudio
$ with env active sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && pip3 install pyaudio
```

# For the gi error
```
$ virtualenv users

$ pip install vext
$ pip install vext.gi

$ other answers
$ 1 -sudo apt-get install python3-gi

$ 2 - sudo apt-get install pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev
$     pip3 install gobject PyGObject
```