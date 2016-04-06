import speech_recognition as sr #Import the speech recognition library
#Setup speech
r = sr.Recognizer()
#Code to get speech
with sr.Microphone() as source:
	print("Input equation:")
	audio = r.listen(source) #Sets a variable called audio to the audio input, to be later interpreted

dict = {"what is": " ", "plus": "+", "added to": "+", "minus":"-", "subracted by": "-", "divided by":"/", "multiplied by" : "*", "x" : "*", "times":"*","parenthesis": "parentheses", "in parentheses" : "(", "end parentheses" : ")", "parentheses" : ")", "negative": "-","to the power" : "**"}

#Below are the try and except blocks for google speech recognition

try:
	equation = r.recognize_google(audio).lower() #Takes whatever the speech interpretor took the input as and makes it lower case to fit the dictionary
	#equation = raw_input("Input equation: ") # For typing in equation
	print(equation)
	for key in dict: #Goes through the equation replacing any phrases with their mathematical equivalents
		equation = equation.replace(key, dict[key])

	try:
		ev = eval(equation) #eval is a standard evaluating function in python. Later it should be replaced with a manual evaluator
		print(equation)
		print(ev)
	except: #In case the input doesn't explicitly state an end parentheses, adds one
		try:
			equation = equation + ")" #Add a paren to the end
			ev = eval(equation) 
			print(equation)
			print(ev)
		except:
			print("Unable to evaulate equation")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio") #The two excepts below are the standard for google speech recognition
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))