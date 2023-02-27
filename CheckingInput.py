def correct_int() -> int:
    """Ввод целого числа с обработкой некорректного введения"""
    is_correct = True
    while is_correct:
        num_int = input()
        try:
            num_int = int(num_int)
            is_correct = False
            return num_int
        except ValueError:
            print("Это не целое число. Введите снова:")
