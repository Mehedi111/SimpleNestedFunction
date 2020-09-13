def calculator(operation):
    if operation == "add":
        def add(p1, p2):
            return p1 + p2
        return add
    elif operation == "sub":
        def sub(p1, p2):
            return p1 - p2
        return sub
    elif operation == "mul":
        def mul(p1, p2):
            return p1 * p2
        return mul
    elif operation == "mul":
        def div(p1, p2):
            return p1 / p2
        return div
    else:
        return "No operation found"

user_operation = input('Which operation you wanna do ?')
operation = calculator(user_operation)
if isinstance(operation, str):
    print(operation)
else: 
    val_one = int(input("Enter frist number : "))
    val_two = int(input("Enter second number : "))
    print(operation(val_one, val_two))
