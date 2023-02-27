import random

from checkingInput import correct_int

# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливый ли билет.
# Пример:
# 385916 -> yes
# 123456 -> no

print("Номер билета: ", end='')
ticket_num = correct_int()

while ticket_num < 100000 or ticket_num >= 1000000:
    if ticket_num < 100000:
        rand = random.randint(0, 10)
        ticket_num = ticket_num * 10 + rand
    if ticket_num >= 1000000:
        ticket_num = ticket_num // 10
right = ticket_num // 1000
left = ticket_num % 1000
res_right = 0
res_left = 0
while right >= 1 and left >= 1:
    temp1 = right % 10
    res_right += temp1
    right //= 10
    temp2 = left % 10
    res_left += temp2
    left //= 10
if res_right == res_left:
    print(f"Билет с номером {ticket_num} - счастливый!")
else:
    print(f"Билет с номером {ticket_num} - не счастливый!")
