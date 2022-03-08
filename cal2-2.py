while True:
    a = input("1st input?")

    if a == "0000":
        break
    b = int(input("2nd input?"))
    a = int(a);

    result = a + b
    print(a, "+", b, "=", result)
    result = a - b
    print(a, "-", b, "=", result)
    result = a * b
    print(a, "*", b, "=", result)
    result = a / b
    print(a, "/", b, "=", result)

print("END")