# all the functions defined in calculator.py is called or imported here.

from calculator import add 
from calculator import subtract
from calculator import multiply
from calculator import divide

# A main function is defined.It presents a menu of available operations and prompts the user to choose one. 
# Depending on the user's selection, the script requests two numbers and executes the chosen operation by invoking the relevant function.
# Following the display of the result, the script inquires whether the user wishes to perform another calculation. This loop continues 
# until the user opts to conclude the calculations by entering 'no'.

def main():
    print("Enter your selection of the functionality")
    print(" 1. add\n 2. subtract\n 3. multiply\n 4. Division")

    while True:
        choice = input("Enter your preferred functionality (1,2,3,4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter number1: "))
            num2 = float(input("Enter number2: "))
            
            process(choice, num1, num2)
            next_calculation = input("Do you want to proceed (y/n): ")
            if next_calculation.lower() != 'y':
                break
        else:
            print("Rectify the entered input and enter again")

#process is defined 
            
def process(choice, num1, num2):
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")        #for addition
    
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")   #for subtraction
    
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")   # for multiplication
    
    elif choice == '4':
        outcome = divide(num1, num2)                         # for division
    
        if outcome == "Infinite result !! Division by zero NOT POSSIBLE":    
            print(outcome)
        else:
            print(f"{num1}/{num2} = {outcome}")

if __name__ == "__main__":
    main()

