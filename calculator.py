# building a Calculator v1.0 as my fisrt project ...I have learnt al the basics already years ago ...it's not a big deal to build it , I just want structure to my Git repo,

# Phase 1 : Basic structure
# while True:
    
#         first_num = float(input("Enter your first value here...  "))
#         second_num = float(input("Enter your second value here...  "))

#         operator = input("Enter your operation type...(+ - * /): ")

#         if operator== "+":
#                 print("The Required Sum is : ", first_num+second_num)

#         elif operator=="-":
#                 print("The Subtracted Value is : ", first_num-second_num)

#         elif operator=="*":
#                 print("The Multiplication Gives : ", first_num*second_num)

#         elif operator== '/':
#                 try:
#                     result=first_num/second_num

#                 except ZeroDivisionError:
#                        print('e')



### FINAL ANSWER    Try 3.....version 1.0
'''
def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"


while True:
    try:
        first_num = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        second_num = float(input("Enter second number: "))

        result = calculate(first_num, operator, second_num)
        print(f"{first_num} {operator} {second_num} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator closed.")
        break



'''




#Calculator v2.0 with new features : Power and Modulus operators and also a history of calculations

# ========== NEW FEATURE 1 & 2: Power and Modulo operators ==========
def calculate(a, op, b):
    """Performs the chosen arithmetic operation."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    # NEW: Power operator (a ^ b)
    elif op == "^":
        return a ** b
    # NEW: Modulo operator (a % b)
    elif op == "%":
        if b == 0:
            return "Error: Modulo by zero"
        return a % b
    else:
        return "Invalid operator"

# ========== NEW FEATURE 3: Calculation history ==========
history = []   # List to store past calculations (each as a string)

while True:
    try:
        first_num = float(input("Enter first number: "))
        # Updated prompt to include new operators
        operator = input("Enter operator (+ - * / ^ %): ")
        second_num = float(input("Enter second number: "))

        result = calculate(first_num, operator, second_num)

        # Build the full calculation string
        calc_str = f"{first_num} {operator} {second_num} = {result}"
        print(calc_str)

        # NEW: Store only successful (non-error) results in history
        if isinstance(result, (int, float)) and "Error" not in str(result):
            history.append(calc_str)

    except ValueError:
        print("Error: Please enter valid numbers")

    # ========== NEW: Option to view calculation history ==========
    view_hist = input("View calculation history? (y/n): ").lower()
    if view_hist == 'y':
        if not history:
            print("No calculations in history yet.")
        else:
            print("\n--- Calculation History ---")
            for idx, entry in enumerate(history, start=1):
                print(f"{idx}. {entry}")
            print("---------------------------\n")

    # Continue or exit (original behaviour preserved)
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator closed.")
        break


























#trial code for functions and error handling

# def add():
#     if operator=="+":
#         return first_num + second_num
#     print("Your Required Sum is : ", first_num + second_num )
    


# def subtraction():
#     if operator=="-":
#         return first_num - second_num
#     print("The subtracted value is : ", first_num - second_num )
    

# def multiply():
#     if operator=='*':
#         return first_num * second_num
#     print('The multiplied value is :', first_num * second_num)
    

# def divide():
#     if operator=='/':
#         try:
#             result = first_num/second_num
#         except ZeroDivisionError:
#             print('e')

               
    

# divide()
# add()
# subtraction()
# multiply()
