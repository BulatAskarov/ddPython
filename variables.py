name = input("Name: ")
age = float(input("Age: "))
isWorking = input("Is Working? (1 or 0)") == "1"
workPlace = None

if isWorking:
    workPlace = input("Work place: ")

if isWorking and not workPlace:
    print("Work Place is null!")

if age > 20:
    print("age > 20")
elif age >= 18:
    print(f"{name} is adult")
else:
    print(f"{name} is not adult")

print(f"Name: {name}")
print(str(age))
print(str(isWorking))
print(workPlace)

str_template = "Информация: {0} - {1}"
print(str_template.format(name, age))


print(name.upper())
print(name.lower())
print(name.find("a"))
print(name.replace("e", "a"))
print(name)

# a = 2
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
#
#
# number = input("Enter number:")
# number = int(number)
# print(number * 2)
#
#
# c = 4
# c += 1
