RED = '\x1b[41m'
BLUE = '\u001b[44m'
WHITE = '\x1b[48;5;15m'
END = '\u001b[0m'


def draw_line(color, ln):
    line = ' ' * ln
    print(color, line, END)


def Flag_Netherlands():
    print('Ex 1 (Netherlands flag)')
    for color in [RED, WHITE, BLUE]:
        draw_line(color, 20)
    print('\n'*2)


def Tracery_c():
    print('Ex 2 (Tracery c)')
    print(WHITE, END, " " * 8, WHITE, WHITE, END, " " * 8, WHITE, END)
    for i in range (4):
        print(" " * i, WHITE, END, " " * (6 - 2 * i), WHITE, END, " " * i * 2, WHITE, END, " " * (6 - 2 * i), WHITE, END)

    print(" " * 4, WHITE, WHITE, END, " " * 8,  WHITE, WHITE, END)

    for i in range (3, -1, -1):
        print(" " * i, WHITE, END, " " * (6 - 2 * i), WHITE, END, " " * i * 2, WHITE, END, " " * (6 - 2 * i), WHITE, END)
    print(WHITE, END, " " * 8, WHITE, WHITE, END, " " * 8, WHITE, END)

    print('\n'*2)


def graph():
    print('Ex 3 (function y(x) = 2*x)\n')
    print('    OY')
    spaces_after_OY = 12
    OY_coordimates = 30
    OX_coordinates = 15
    spaces_before_x = 1
    for i in range(20):
        while OY_coordimates >= 10:
            print(f'{OY_coordimates} ', WHITE, END, ' ' * spaces_after_OY, WHITE, END, spaces_before_x * ' ', f'(x = {OX_coordinates})')
            spaces_after_OY -= 1
            OY_coordimates -= 2
            OX_coordinates -= 1
            spaces_before_x += 1
        while 4 < OY_coordimates < 10:
            print(f'{OY_coordimates}  ', WHITE, END, ' ' * spaces_after_OY, WHITE, END, spaces_before_x * ' ', f'(x = {OX_coordinates})')
            spaces_after_OY -= 1
            OY_coordimates -= 2
            OX_coordinates -= 1
            spaces_before_x += 1
    print('\n'*2)


def diagram():
    print('Ex 4 (diagram)')
    with open('sequence.txt') as f:
        data = [abs(float(x)) for x in f]

    sum_chet_pos, sum_nechet_pos = 0, 0
    for i in range(len(data)):
        if (i+1) % 2 == 0:
            sum_chet_pos += data[i]
        else:
            sum_nechet_pos += data[i]
    sum_all = sum(data)
    percent_ratio_chet = sum_chet_pos * 100 / sum_all
    percent_ratio_nechet = sum_nechet_pos * 100 / sum_all
    a, b = round(percent_ratio_chet, 2), round(percent_ratio_nechet, 2)

    print(f'Чётные числа: {a}          Нечётные числа: {b}')
    if a > b:
        for i in range(max((a - b) / 10, 1)):
            print(WHITE, ' ', END)
        for i in range(10 - max((a - b) / 10, 1)):
            print(WHITE, ' ', END, ' ' * 24, WHITE, ' ', END)
    else:
        for i in range(max((b - a) / 10, 1)):
            print(' ' * 28, WHITE, ' ', END)
        for i in range(10 - max((b - a) / 10, 1)):
            print(WHITE, ' ', END, ' ' * 24, WHITE, ' ', END)


Flag_Netherlands()  # Ex. 1
Tracery_c()         # Ex. 2
graph()             # Ex. 3
diagram()           # Ex. 4