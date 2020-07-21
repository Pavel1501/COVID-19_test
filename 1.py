try:
	print ("Attention, the program will make an examplary result that doesn`t certanly mean that you are ill or you are not")
	print ("Good luck :)")
	result = 10
	name = input('Enter your name...')
	print ("Hello," + name)
	
	so = int(input('Are you ready?\n 1 - Yes\n 2 - No\n '))
	if so == 1:
		print("Let's start")
		print('Ok, take a thermometer and measure your temperature')


		temp = float(input('Write down your result\n'))
		if temp >= 37.0:
			print ('The result is not really good but don`t worry')
			result -= 1
		elif temp <= 36.4:
			print('You have a weakness, you need to worry')
			result -= 1
		elif 36.9 >= temp >= 36.5:
			print('Everything is fine ;)')
			result += 1
		else:
			print("You entered unknown result")
		print("Ok," + name + " let's continue")


		print ('Have you been feeling tired recently?')
		week = int(input('Enter 1 if you have and 2 if you haven`t \n' ))
		if week == 1:
			print('That`s not really good but I won`t make you feel scary')
			result -=1 
		elif week == 2:
			print("Ohhh that`s really cool")
			result += 1
		else:
			print("You entered unknown result")
		print ("Let's continue")


		food = int(input('Have you noticed a loss of appetite?\n 1 - if you have\n 2 - if you haven`t\n '))
		if food == 1:
			print ('Anything can happen, we hope that everything will be fine...')
			result-=1
		elif food ==2:
			print("Perfect!!!")
			result +=1
		else:
			print("You entered unknown result")
		print ('And now the last but not the least')


		cough =int(input('Do you have cough?\n 1 - if you do\n 2 - if you don`t\n '))
		if cough == 1:
			result -= 1
			print("It's bad but don't despair")
		elif cough == 2:
			result += 1
			print('Great! Waiting for the results')
		else:
			print("You entered unknown result")
		print("Ok, it's time to sum everything up...\n")


		if result == 14:
			print("Everything is perfect, you don`t need to worry")
		elif result == 11 or result == 12 or result == 10:
			print("Ok, you have some symptoms of COVID-19 but don`t worry, isolate yourself for some period of time and if your situation doesn't get better, call a doctor")
		elif result == 9 or result == 8: 
			print('Don`t panic, isolate yourself and call a doctor today')
		elif result == 6:
			print("Call a doctor immediately!!!")
	elif so == 2:
		print("Ok, as you wish but be careful")
	else:
		print("You entered unknown result")





except ValueError:
	print ("Something went wrong")
