a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))


def sum_max (var1, var2, var3):
   my_list = [var1, var2, var3]
   my_list.sort()
   return (my_list[1] + my_list[2])


print (sum_max(a, b, c))





