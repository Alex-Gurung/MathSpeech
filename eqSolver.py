import speech_recognition as sr #Import the speech recognition library
from sympy import * #Necessary for commented out code, but comment this import if not using them
#Setup speech
r = sr.Recognizer() #Creates a variable to listen to the audio
#Code to get speech

with sr.Microphone() as source: #Need this block every time you want to input speech
	#print("Do you want to solve an expression or solve for a variable?") #To be implemented lated with sympy
	print("Say your equation:")
	#audio = input("Input your equation") #For text input, can be moved outside of with statement
	#x = Symbol('x')
	#diff(audio, x)						#For direct derivative typed input
	audio = r.listen(source) #Sets a variable called audio to the audio input, to be later interpreted