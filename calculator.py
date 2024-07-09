first_number = int(input("insert first number: "))
while True:
    work = input("what do you want to do (+,-,*,/,=,C): ")
    second_number = int(input("whats your second number: "))
    if work == "+":
        first_number = first_number + second_number
    elif work == "-":
        first_number = first_number - second_number
    elif work == "*":
        first_number = first_number * second_number
    elif work == "/":
        first_number = first_number // second_number
    elif work == "=":
        print(f"its equale {first_number}")
        break
    elif work == "C":
        break