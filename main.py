import speech_recognition as sr
#Setup speech
r = sr.Recognizer()
#Code to get speech
with sr.Microphone() as source:
	print("Input equation:")
	audio = r.listen(source)
dict = {"plus": "+", "added to": "+", "minus":"-", "subracted by": "-", "divided by":"/", "multiplied by" : "*", "x" : "*", "times":"*", "parenthesis": "parentheses", "in parentheses" : "(", "end parentheses" : ")", "parentheses" : ")", "negative": "-", "to the power": "**"}
#Below are the try and except blocks for google speech recognition
try:
	equation = r.recognize_google(audio).lower()
	#equation = raw_input("Input equation: ") # For typing in equation
	print(equation)
	for key in dict:
		equation = equation.replace(key, dict[key])

	try:
		ev = eval(equation)
		print(equation)
		print(ev)
	except:
		try:
			equation = equation + ")"
			ev = eval(equation)
			print(equation)
			print(ev)
		except:
			print("Unable to evaulate equation")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))