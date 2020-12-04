#Program's Menu
def menu():
	print("\t\t\tWelcome to Minimal Calculator\n")
	print("1) Addition.")
	print("2) Subtraction.")
	print("3) Multiplication.")
	print("4) Division.")
	print("5) Exit.\n")

	option = input("\nEnter an option -> ")

	if option != "5":
		number_1 = input("\nNumber 1: ")
		number_2 = input("Number 2: ")

		return option, number_1, number_2

	return option

#Program's Utilities
def addition(number_1, number_2):
	plus = float(number_1) + float(number_2)
	return plus

def subtraction(number_1, number_2):
	minus = float(number_1) - float(number_2)
	return minus

def multiplication(number_1, number_2):
	times = float(number_1) * float(number_2)
	return times

def division(number_1, number_2):
	divided = float (number_1) / float(number_2)
	return divided

#Main program
def calculator():

	again = "n"

	try:
		option, number_1, number_2 = menu()
	except ValueError:
		option = "5"

	try:
		if option == "1":
			print(addition(number_1, number_2))
		elif option == "2":
			print(subtraction(number_1, number_2))
		elif option == "3":
			print(multiplication(number_1, number_2))
		elif option == "4":
			print(division(number_1, number_2))
		elif option == "5":
			return again == "n"
		elif option != ("1" or "2" or "3" or "4" or "5"):
			print("\nUps! That is not an option. Plase, try again...\n")
			calculator()

		for i in range(1,5):
			if option == str(i):
				again = input("Do you wanna try again? (y/n): ")
				print("\n")
				return again
				break
			else:
				return again

	except ValueError:
		print("\nUps! Nothing happends. Are you sure that your numbers are rigth? Try Again...\n")

again = calculator()

while again == ("y" or "Y"):
	calculator()

print("\n\t\t\tThanks for use the Minimal Calculator!")
input("\nType any key and press Enter to continue... ")
