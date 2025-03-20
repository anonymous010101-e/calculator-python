# Simple Python Calculator!

#Welcome message.
print("Welcome to the calculator! This small program was made in Python! \n")


#Function for the calculator, and error handler.
def calculator():
    try:
        num1 = float(input("Enter a number: "))
        op = input("enter an operator (+, -, *, /): ")
        num2 = float(input("Enter another number: \n"))
    
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("Sorry, invalid operator, try again :/")

    except:
        print("Sorry, something went wrong, try again.")
        if True:
            return None


calculator()



'''
Second function prompting the user another try, this function keeps the program running
until the user wants to end it.

'''

def repeat_calc():
    while True:
        try_again = input("Would you like to try again? (Y/N): ")
        if try_again.lower() == "y":
            print(calculator())
        elif try_again.lower() == "n":
            print("Thank you for using the calculator! Goodbye! :)")
        else:
            print("Not Y or N, try again :/")
            break
        

repeat_calc()


#I'm aware this could've been more efficient, again, just doing quick basic projects for practice, thank you and enjoy.


#By Anonymous on Github.
