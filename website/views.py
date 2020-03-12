#import the django library that renders views in our website 
from django.shortcuts import render

#create and return a view for the home.html webpage
def home(request):
	return render(request, 'home.html', {})

#create and return a view for the add.html webpage
def add(request):
	#import the python random library to generate random numbers
	from random import randint

	#create 2 random integers and store them as variables
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	#if the user types an answer into the form
	if request.method == "POST":
		#recieve their answer and the 2 random integers
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		#if the user has not entered an answer in the form
		#rederict to the original page
		if not answer:

			my_answer = "You Forgot To Input A Number!"
			color = 'danger'

			return render(request, 'add.html', {
			'color':color,
			'my_answer':my_answer,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		#store the correct answer in a variable
		correct_answer = int(old_num_1) + int(old_num_2)
		
		#if the user's answer is correct/incorrect alert them
		#colour is green if correct
		#colour is red if incorrect
		if int(answer) == correct_answer:
			my_answer = "Correct!" + " " + old_num_1 + " + " + old_num_2 + " = " + answer
			color = "success"
		else:
			my_answer = "Incorrect!" + " " + old_num_1 + " + " + old_num_2 + " = "  + str(correct_answer) + " (You Answered: " + answer + ")"
			color = "danger"

		return render(request, 'add.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	#return the view, and 2 random integers to the add.html page
	return render(request, 'add.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

#create and return a view for the subtract.html webpage
def subtract(request):
	#import the python random library to generate random numbers
	from random import randint

	#create 2 random integers and store them as variables
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	#if the user types an answer into the form
	if request.method == "POST":
		#recieve their answer and the 2 random integers
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		#if the user has not entered an answer in the form
		#rederict to the original page
		if not answer:

			my_answer = "You Forgot To Input A Number!"
			color = 'danger'

			return render(request, 'subtract.html', {
			'color':color,
			'my_answer':my_answer,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		#store the correct answer in a variable
		correct_answer = int(old_num_1) - int(old_num_2)
		
		#if the user's answer is correct/incorrect alert them
		#colour is green if correct
		#colour is red if incorrect
		if int(answer) == correct_answer:
			my_answer = "Correct!" + " " + old_num_1 + " - " + old_num_2 + " = " + answer
			color = "success"
		else:
			my_answer = "Incorrect!" + " " + old_num_1 + " - " + old_num_2 + " = "  + str(correct_answer) + " (You Answered: " + answer + ")"
			color = "danger"

		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	#return the view, and 2 random integers to the add.html page
	return render(request, 'subtract.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

#create and return a view for the multiply.html webpage
def multiply(request):
	#import the python random library to generate random numbers
	from random import randint

	#create 2 random integers and store them as variables
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	#if the user types an answer into the form
	if request.method == "POST":
		#recieve their answer and the 2 random integers
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		#if the user has not entered an answer in the form
		#rederict to the original page
		if not answer:

			my_answer = "You Forgot To Input A Number!"
			color = 'danger'

			return render(request, 'multiply.html', {
			'color':color,
			'my_answer':my_answer,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		#store the correct answer in a variable
		correct_answer = int(old_num_1) * int(old_num_2)
		
		#if the user's answer is correct/incorrect alert them
		#colour is green if correct
		#colour is red if incorrect
		if int(answer) == correct_answer:
			my_answer = "Correct!" + " " + old_num_1 + " x " + old_num_2 + " = " + answer
			color = "success"
		else:
			my_answer = "Incorrect!" + " " + old_num_1 + " x " + old_num_2 + " = "  + str(correct_answer) + " (You Answered: " + answer + ")"
			color = "danger"

		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	#return the view, and 2 random integers to the multiply.html page
	return render(request, 'multiply.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

#create and return a view for the divide.html webpage
def divide(request):
	#import the python random library to generate random numbers
	from random import randint

	#create 2 random integers and store them as variables
	num_1 = randint(0,10)
	num_2 = randint(1,10)

	#if the user types an answer into the form
	if request.method == "POST":
		#recieve their answer and the 2 random integers
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		#if the user has not entered an answer in the form
		#rederict to the original page
		if not answer:

			my_answer = "You Forgot To Input A Number!"
			color = 'danger'

			return render(request, 'divide.html', {
			'color':color,
			'my_answer':my_answer,
			'answer':answer,
			'num_1':num_1,
			'num_2':num_2,
			})

		#store the correct answer in a variable
		correct_answer = int(old_num_1) / int(old_num_2)
		
		#if the user's answer is correct/incorrect alert them
		#colour is green if correct
		#colour is red if incorrect
		if float(answer) == correct_answer:
			my_answer = "Correct!" + " " + old_num_1 + " / " + old_num_2 + " = " + answer
			color = "success"
		else:
			my_answer = "Incorrect!" + " " + old_num_1 + " / " + old_num_2 + " = "  + str(correct_answer) + " (You Answered: " + answer + ")"
			color = "danger"

		return render(request, 'divide.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})

	#return the view, and 2 random integers to the divide.html page
	return render(request, 'divide.html', {
		'num_1':num_1,
		'num_2':num_2,
		})

