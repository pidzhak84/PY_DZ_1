# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример: 123 -> 6 (1 + 2 + 3), 100 -> 1 (1 + 0 + 0).

number = int(input("Введите трехзначное число - "))
summa = 0
while number > 0:
    n = number % 10
    summa = summa + n
    number = number // 10
print("Сумма цифр этого числа = ", summa)