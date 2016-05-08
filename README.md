# MathSpeech
A splinter project from PythonSpeechRecognition, this is an attempt to use speech recognition(in python) to solve math problems spoken normally(As one would normally say the problem).
##Setup
Speech recognition is done through a python library, found here: [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/). You will also need pyaudio, which can be installed using pip('pip install pyaudio') or direct download. Make certain everything is up to date to avoid issues.
##How to Run
In order to use/test the program, just run the main.py file and when it outputs "Input equation:" say your equation. It should then output what it thought you said, the mathematical equivalent, and the result. The speech recognition part may take a while depending on clarity of speech and surrounding noise. Make sure to look into the code if you want to change functionality(like type in the equation for testing), as there is a lot of commented code that you can use
