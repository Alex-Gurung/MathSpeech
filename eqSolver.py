import speech_recognition as sr #Import the speech recognition library
from sympy import * #Necessary for commented out code, but comment this import if not using them

def eqSolver():
	#Setup speech
	r = sr.Recognizer() #Creates a variable to listen to the audio
	#Code to get speech

	with sr.Microphone() as source: #Need this block every time you want to input speech
		#print("Do you want to solve an expression or solve for a variable?") #To be implemented lated with sympy
		print("Say your equation(with variable z):")
		#audio = input("Input your equation") #For text input, can be moved outside of with statement
		#x = Symbol('x')
		#diff(audio, x)						#For direct derivative typed input
		audio = r.listen(source) #Sets a variable called audio to the audio input, to be later interpreted
	
	z = Symbol('z') #Because speech recognition sometimes uses 'x' as 'times', z must be used
	####BELOW CODE SHOULD BE CHANGED
	try:
		equation = r.recognize_google(audio).lower() #Takes whatever the speech interpretor took the input as and makes it lower case to fit the dictionary
		print(equation) #Prints the equation, check to see if it recognized your speech correctly
		for i in range(len(keys)): #Goes through the equation replacing any phrases with their mathematical equivalents
			equation = equation.replace(keys[i], results[i])
		equation = equation.strip() #Removes unnecessary splaces at ends(shouldn't change anything)
	except sr.UnknownValueError: #This is the most common error, try audio again, making certain the program can clearly hear you
	    print("Google Speech Recognition could not understand audio") #The two excepts below are the standard for google speech recognition
	    return
	except sr.RequestError as e: #Make sure to keep these excepts whenever calling recognize_google(audio)
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    return

	print(solve(equation, z)) #Solves the equation with a variable 'z' NOTE: must use 'z' and only 'z' as variable