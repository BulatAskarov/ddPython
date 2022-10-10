lst = [1, 2, 3]
lst.append(4)
lst.remove(3)

print(lst)
print(lst[0])
print(lst[-1])

if 2 in lst:
    print("2 in list")
else:
    print("2 is not in list")

lst_console = input("Enter list via space: ")
numbers = lst_console.split(" ")
print(numbers)

tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

first, second, third = tup
print("1", first)
print("2", second)
print("3", third)

print(3 in tup)



eng_rus_dict = {
    "cat": "кот",
    "car": "машина"
}

print(eng_rus_dict)
print(eng_rus_dict['cat'])
eng_rus_dict['cat'] = 'Кошка'
print(eng_rus_dict['cat'])

print("car" in eng_rus_dict)
print(eng_rus_dict.values())
print("кот" in eng_rus_dict.values())
print(eng_rus_dict.keys())
print(eng_rus_dict.items())

print(eng_rus_dict.get("brother", "(нет перевода)"))

set_from_lst = set(lst)
set_example = {1, 2, 3}
print(set_example)
print(set_from_lst)

set_example.add(5)
set_example.remove(2)
print(set_example)
print(set_example - {3, 5})
print(set_example.union({6, 7}))
print(set_example == {1, 5, 3})

print(len("брат"))
print(len(lst))
print(len(eng_rus_dict))
print(len(set_example))