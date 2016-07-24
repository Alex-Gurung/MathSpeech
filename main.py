import speech_recognition as sr #Import the speech recognition library
#from eqSolver import eqSolver
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

######################################
#EQUATION CODE FOR FUTURE WORK
#equation = input("Input your equation: \n") #Uncomment to test this code
#x = Symbol('x')
#print(solve(equation, x)) #Solves the equation with a variable 'x' NOTE: must use 'x' and only 'x' as variable
#equation.replace("y", "")
#equation.replace("=", "")
################SAMPLE CODE######################
#limit(sin(x)/x, x, 0) #LIMIT
#integrate(exp(x)*sin(x) + exp(x)*cos(x), x) #INTEGRAL
#diff(sin(x)*exp(x), x) #DERIVATIVE
#if ("equation" in equation): 	###May not use
#	##Switch to equation solvers, else, continue with basic solving
#	eqSolver()
#else:
#	#do the eval() stuff

keys = [line.rstrip('\n') for line in open('keys.txt')] #Puts every line in keys.txt in a list, split by "\n"
results = [line.rstrip('\n') for line in open('results.txt')] #Same thing, but for results.txt
#Below are the try and except blocks for google speech recognition

try:
	equation = r.recognize_google(audio).lower() #Takes whatever the speech interpretor took the input as and makes it lower case to fit the dictionary
	print(equation) #Prints the equation, check to see if it recognized your speech correctly
	for i in range(len(keys)): #Goes through the equation replacing any phrases with their mathematical equivalents
		equation = equation.replace(keys[i], results[i])
	equation = equation.strip() #Removes unnecessary splaces at ends(shouldn't change anything)
	try:
		ev = eval(equation) #eval is a standard evaluating function in python. Later it should be replaced with a manual evaluator
		print(equation) #Prints the equation, given that it can be evaluated
		print(ev) #Prints the evaluated output
	except: #In case the input doesn't explicitly state an end parentheses, adds one
		try:  # THIS SHOULD BE CHANGED LATER
			equation = equation + ")" #Add a paren to the end
			ev = eval(equation) #Attemps to evaluate again
			print(equation) #Prints the equation
			print(ev) #Prints the evaluation
		except: #If it isn't just missing an end paren... 
			print("Unable to evaulate equation") #say unable to evaluate
except sr.UnknownValueError: #This is the most common error, try audio again, making certain the program can clearly hear you
    print("Google Speech Recognition could not understand audio") #The two excepts below are the standard for google speech recognition
except sr.RequestError as e: #Make sure to keep these excepts whenever calling recognize_google(audio)
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
