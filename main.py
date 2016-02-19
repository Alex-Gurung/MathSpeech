import speech_recognition as sr
#Setup speech
r = sr.Recognizer()
#Code to get speech
with sr.Microphone() as source:
	print("Input equation:")
	audio = r.listen(source)

#Below are the try and except blocks for google speech recognition
try:
	equation = r.recognize_google(audio).lower()
	print(equation)
	equation = equation.replace("plus", "+")
	equation = equation.replace("added to", "+")
	equation = equation.replace("minus", "-")
	equation = equation.replace("subracted by", "-")
	equation = equation.replace("divided by", "/")
	equation = equation.replace("multiplied by", "*")
	equation = equation.replace("x", "*")
	equation = equation.replace("times", "/")
	equation = equation.replace("parenthesis", "parentheses")
	equation = equation.replace("in parentheses", "(")
	equation = equation.replace("end parentheses", ")")
	equation = equation.replace("parentheses", ")")
	equation = equation.replace("negative", "-")
	equation = equation.replace("to the power", "**")
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