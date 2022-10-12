def test(a, b, *args, is_test=True, **kwargs):
    print("простые аргументы:", a, b)
    print("args", args)
    print("is test", is_test)
    print("kwargs", kwargs)


test(1, 2, 3, 4, 5, is_test=False, message="test message")

