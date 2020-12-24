a = 2
b = 3
n = 1
while True:
    a = a * 0.1 + a
    print(f"{n}-й день: {a}")
    n += 1
    if a >= b:
        break
