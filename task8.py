from checkingInput import correct_int

# Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print("Размер шоколадки по горизонтали: ", end='')
h_size = correct_int()
print("Размер шоколадки по вертикали: ", end='')
v_size = correct_int()
print("Сколько долек вам нужно: ", end='')
num_slices = correct_int()
if num_slices >= h_size * v_size:
    print("Можно и так, но лишний вес до добра не доводит.")
if num_slices % h_size == 0 or num_slices % v_size == 0:
    print(f"Вот ваши {num_slices} дольки(ек).")
else:
    print("Всё. Весь шоколад съели.")
