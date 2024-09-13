def getmultiplieddigits(number):
    strnumber = str(number)

    if len(strnumber) > 1:
        first = int(strnumber[0])
        return first * getmultiplieddigits(int(strnumber[1:]))
    else:
        return int(strnumber)

# Проверка
result = getmultiplieddigits(40203)
print(result)  # Вывод: 24
