# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def Truth ():
    result = 0
    for n in range(0, 8):
        num = bin(n)
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        left_part = not(X or Y or Z)
        right_part = (not X) and (not Y) and (not Z)
        if left_part == right_part:
            result += 1
        print(X, Y, Z, left_part, right_part, left_part == right_part, result)
    print()
    if result == 8:
        return print(True)
    else:
        return print(False)

Truth()