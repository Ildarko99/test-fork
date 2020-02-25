'''4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

number = int(input('Введите число \n'))
result = 0
def maximum_number (x):
    result = 0
    if x < 10:
        return x
    else:
        while x != 0:
            y = x % 10
            if y > result:
                result = y
            x = x // 10
        return result
print(maximum_number(number))
# result = 0
#
# while number //

# yah, we are on github?! pushed by PyCharm
# yeahhh! pushed by bash