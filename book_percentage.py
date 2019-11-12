end_page = 432.0
start_page = 1.0
total_page = end_page - start_page
while True:
	user_current_page = ("\nThe total page is " + str(total_page))
	user_current_page += ("\nWhich page are you on? ")
	user_current_page = input(user_current_page)
	user_current_page = int(user_current_page)
	book_percentage_not_rounded = ((user_current_page/total_page) * (100))
	# book_percentage_rounded = round((user_current_page/total_page) * (100))

	print("\n" + "You've read " + str(book_percentage_not_rounded) + "%" + " of the book")
	if str(book_percentage_not_rounded) == 'quit':
		break
	elif book_percentage_not_rounded == 50.0:
		print("Congratulations! You finished half of the book.")
		print("You have " + str(end_page-user_current_page) + " pages left.\n")

	elif book_percentage_not_rounded > 50.0: 
		print("Congratulations! You finished more than half of the book.")
		print("You have " + str(end_page-user_current_page) + " pages left.\n")

	else: 
		print("Keep going.")
		print("You have " + str(end_page-user_current_page) + " pages left.\n")


	# Part 2: How many page is 20% 30% 40% 50%?
	user_percentage = input("Enter the percentage you'd like to read to ")
	user_percentage = int(user_percentage)
	pages_read = (user_percentage/100.0) * (end_page)
	print("If you want to read to " + str(user_percentage) + "%" 
		+ " then you will need to read " + str(pages_read) + " pages.")

