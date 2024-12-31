# инициализация входных данных
numbers = [100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# сортируем начальный список для избежания ошибок в процессе работы программы
numbers.sort()
# начало цикла (перебор начального списка)
for i in range(len(numbers)):
    is_prime = True                         # установка флага
    if numbers[i] == 1:                     # исключаем "1"
        continue
    for j in range(2, i):                   # цикл перебора числа по делителям
        if numbers[i] % j == 0:             # проверка на делимость
            is_prime = False                # установка флага
            break
    if is_prime:                            # добавление числа в конечные списки
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

# вывод результата
print(primes)
print(not_primes)