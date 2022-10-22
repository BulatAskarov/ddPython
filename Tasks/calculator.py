additions = []
subtractions = []
multiplications = []
divisions = []
while (True):
    a = int(input("Введите а: "))
    b = int(input("Введите б: "))
    action = input("Введите операцию: ")
    if "+" in action:
        print(a + b)
        additions.append(f"{a}+{b}={a + b}")
    if "-" in action:
        print(a - b)
        subtractions.append(f"{a}-{b}={a - b}")
    if "*" in action:
        print(a * b)
        multiplications.append(f"{a}*{b}={a * b}")
    if "/" in action:
        print(a / b)
        divisions.append(f"{a}/{b}={a / b}")
    print(f"+ {additions}")
    print(f"- {subtractions}")
    print(f"* {multiplications}")
    print(f"/ {divisions}")
