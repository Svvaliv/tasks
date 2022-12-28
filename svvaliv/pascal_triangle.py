def pascal_triangle(n: int) -> list[list[int]]:
    array = [[1] + [0] * (n - 1) for _ in range(n)]
    for row in range(1, n):
        for column in range(1, row + 1):
            array[row][column] = array[row - 1][column] + array[row - 1][column - 1]
    return array


n = int(input())
triangle = pascal_triangle(n)
max_len = len(' '.join(map(str, triangle[-1])))
for r in range(n):
    string = ''
    for c in range(r + 1):
        string = string + f'{triangle[r][c]} '
    print(f'{string:^{max_len + 1}}')

