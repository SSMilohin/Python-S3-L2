def make_pascal_triangle(number):
    result = []
    for i in range(number):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


def print_pascal_triangle(pascal_triangle):
    max_width = len(' '.join(map(str, pascal_triangle[-1])))
    for row in pascal_triangle:
        print(' '.join(map(str, row)).center(max_width))


def print_serpinskii_triangle(pascal_triangle):
    last_row_length = len(pascal_triangle[-1])
    max_width = last_row_length * 3
    for row in pascal_triangle:
        new_row = ''
        for item in row:
            if item % 2 != 0:
                new_row += ' * '
            else:
                new_row += '   '
        print(new_row.center(max_width))


n = int(input('Введите число строк треугольника Паскаля: '))
print_pascal_triangle(make_pascal_triangle(n))

m = int(input('Введите количество итераций треугольника Серпинского: '))
for i in range(m):
    print_serpinskii_triangle(make_pascal_triangle(2**(i+1)))
