import speech_recognition as sr #Import the speech recognition library
from sympy import * #Necessary for commented out code, but comment this import if not using them
#Setup speech
r = sr.Recognizer()
#Code to get speech

with sr.Microphone() as source:
	#print("Do you want to solve an expression or solve for a variable?") #To be implemented lated with sympy
	print("Say your equation:")
	#audio = input("Input your equation")
	audio = r.listen(source) #Sets a variable called audio to the audio input, to be later interpreted
######################################
#EQUATION CODE
#equation = input("Input your equation: \n") #Uncomment to test this code
#x = Symbol('x')
#print(solve(equation, x))
#equation.replace("y = ", "")
################SAMPLE CODE######################
#limit(sin(x)/x, x, 0) #LIMIT
#integrate(exp(x)*sin(x) + exp(x)*cos(x), x) #INTEGRAL
#diff(sin(x)*exp(x), x) #DERIVATIVE

dict = {"what is": " ", "plus": "+", "added to": "+", "minus":"-", "subracted by": "-", "divided by":"/", "multiplied by" : "*", "x" : "*", "times":"*","parenthesis": "parentheses", "in parentheses" : "(", "end parentheses" : ")", "parentheses" : ")", "negative": "-","to the power" : "**", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

keys = [line.rstrip('\n') for line in open('keys.txt')]
results = [line.rstrip('\n') for line in open('results.txt')]
#Below are the try and except blocks for google speech recognition

try:
	equation = r.recognize_google(audio).lower() #Takes whatever the speech interpretor took the input as and makes it lower case to fit the dictionary
	#equation = raw_input("Input equation: ") # For typing in equation
	print(equation) #Prints the equation, check to see if it recognized your speech correctly
	for i in range(len(keys)): #Goes through the equation replacing any phrases with their mathematical equivalents
		equation = equation.replace(keys[i], results[i])

	try:
		ev = eval(equation) #eval is a standard evaluating function in python. Later it should be replaced with a manual evaluator
		print(equation)
		print(ev)
	except: #In case the input doesn't explicitly state an end parentheses, adds one
		try:
			equation = equation + ")" #Add a paren to the end
			ev = eval(equation) #Attemps to evaluate again
			print(equation)
			print(ev)
		except:
			print("Unable to evaulate equation") #If all fails, just give up
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio") #The two excepts below are the standard for google speech recognition
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
