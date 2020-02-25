'''Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''
# n = int(input('Input number'))
# result = n
# mult = 11
# print(result)
# for i in range(n-1):
#     print(mult*n)
#     result += mult * n
#     mult = int(str(mult) + '1') #вот тут через преобразование в строку сделал
# print(result)

n = int(input('Input number'))
result = n
mult = 11
mult2 = 100
print(result)
for i in range(n-1):
    print(mult*n)
    result += mult * n
    mult += mult2
    mult2 *= 10
print(result)