from func_tools.divide import divide
from func_tools.sum import sum
from func_tools.subtruct import subtruct
from func_tools.multiply import multiply


# 1) Calculator -> + , * , / , -
# 2) square
# 3) Error handling : try , except , finally

while True:

    operand = input("Enter operand (+, -, *, /, ^2): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operand == '+':
            result = sum(num1, num2)
        elif operand == '-':
            result = subtruct(num1, num2)
        elif operand == '*':
            result = multiply(num1, num2)
        elif operand == '/':
            result = divide(num1, num2)
        else:
            print("!!!Wrong operand!!!")
            continue
        print(f"Result: {num1} {operand} {num2} = ", result)
        is_quit = input("Exit (y): ")
        if is_quit.lower() == 'y':
            exit()
    except ValueError:
        print("!!!Wrong number!!!")
    except NameError:
        print("!!!Wrong number!!!")
