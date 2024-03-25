# Max Yu
# Calulator to add two numbers and display the result


sum = 0 

while True:
    # 1. Input
    print(f"Calculator")
    x1 = input("Enter first number: ")
    x2 = input("Enter second number: ")
    op = input("Enter operator: ")

    # 2. Process
    if op == "+":
        sum = int(x1) + int(x2)
    elif op == "-":
        sum = int(x1) - int(x2)
    elif op == "*":
        sum = int(x1) * int(x2)
    elif op == "/":
        sum = int(x1) / int(x2)

    # 3. Output  
    print(f"Sum: {sum}")
    res = input("Continue? (Y/N)")
    if res == "N":
        break;