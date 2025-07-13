# Переменые для получения челых чисел от пользователя
num1, num2, operation = int(input()), int(input()), int(input())

# Функции операции сложения, вычетания
def plus(a, b): return a + b
def minus(a, b): return a - b

# Вывод резултьта 
print((operation == 1) * plus(num1, num2) or (operation == 2) * minus(num1, num2))
