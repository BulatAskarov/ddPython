st = input()
lst = st.split(" ")
try:
    for k in lst:
        int(k)

    lst2 = [print(i) for i in lst if int(i) % 2 == 0]
    lst3 = [print(i) for i in lst if int(i) % 2 != 0]
    lst4 = [print(i) for i in lst if int(i) < 0]
except ValueError:
    print(-1)


try:
    for k in lst:
        int(k)

    lst2 = filter(lambda x: int(x) % 2 == 0, lst)
    lst2 = list(map(lambda x: print(x), lst2))
    lst3 = filter(lambda x: int(x) % 2 != 0, lst)
    lst3 = list(map(lambda x: print(x), lst3))
    lst4 = filter(lambda x: int(x) < 0, lst)
    lst4 = list(map(lambda x: print(x), lst4))
except ValueError:
    print(-1)
