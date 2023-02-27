from checkingInput import correct_int

# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите любое целое число: ", end='')
number = correct_int()
result = 0
while number >= 1:
    temp = number % 10
    result += temp
    number = number // 10
print("Результат: ", result)
