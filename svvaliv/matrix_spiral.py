# Заполнение матрицы по спирали

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]  # Создаём матрицу размерностью n * m
s = 'right'  # Начальное значение, идём от элемента matrix[0][0] вправо
count = 1  # Счетчик для заполнения матрицы
for i in range(n):
    if count == n * m + 1:  # Если счетчик достиг значения, равного размерности матрицы, значит заполнение закончено и прерываем цикл
        break
    while s == 'right':
        for j in range(i, m):
            if matrix[i][j] == 0:  # Заполняем матрицу вправр, пока не дойдем до границы
                matrix[i][j] = count
                count += 1
            else:  # В противном случае начинаем перемещаться вниз
                s = 'down'
    if n == 1:  # Если у матрицы одна строка, прекращаем заполнение
        break
    while s == 'down':
        for j in range(i + 1, n):
            if matrix[j][-i - 1] == 0:  # Заполняем матрицу вниз, пока не дойдем до границы
                matrix[j][-i - 1] = count
                count += 1
            else:  # В противном случае начинаем перемещаться влево
                s = 'left'
    if m == 1:  # Если у матрицы один столбец, прекращаем заполнение
        break
    while s == 'left':
        for j in range(-i - 1, -m, -1):
            if matrix[-i - 1][j - 1] == 0:  # Заполняем матрицу влево, пока не дойдем до границы
                matrix[-i - 1][j - 1] = count
                count += 1
            else:  # В противном случае начинаем перемещаться вверх
                s = 'up'
    while s == 'up':
        for j in range(n - i - 2, -1, -1):
            if matrix[j][i] == 0:  # Заполняем матрицу вверх, пока не дойдем до границы
                matrix[j][i] = count
                count += 1
            else:  # В противном случае начинаем перемещаться вправо и повторяем цикл
                s = 'right'

# Выводим матрицу на печать
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(4), end=' ')
    print()
