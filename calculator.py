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



### FINAL ANSWER    Try 3

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
