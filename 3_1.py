#  запрашиваем у пользователя делимое и делитель
a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))
def division (var1, var2):
    try:var1 / var2
    except ArithmeticError:
        print("Деление на ноль невозможно! ")
        return
    else: return (var1 / var2)

print (division(a, b))



