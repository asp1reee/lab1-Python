red = '\x1b[41m'
blue = '\u001b[44m'
white = '\x1b[48;5;15m'
end = '\u001b[0m'

#Ex 1 (Netherlands flag)
print('Ex 1 (Netherlands flag)')


def draw_line(color, ln):
    line = ' ' * ln
    print(color, line, end)


for i in [red, white, blue]:
    draw_line(i, 20)


print('\n'*2)

# Ex 2 (Tracery c)
print('Ex 2 (Tracery c)')


print(' ' * 0, white, end, ' ' * 8, white, end,             white * 0, end, ' ' * 6, white, end)
print(' ' * 1, white, end, ' ' * 6, white, end,             white * 1, end, ' ' * 6, white, end)
print(' ' * 2, white, end, ' ' * 4, white, end,    ' ' * 1, white * 1, end, ' ' * 4, white, end)
print(' ' * 3, white, end, ' ' * 2, white, end,    ' ' * 3, white * 1, end, ' ' * 2, white, end)
print(' ' * 4, white, end, ' ' * 0, white, end,    ' ' * 5, white * 1, end, ' ' * 0, white, end)

print(' ' * 5, white, white, end,                  ' ' * 7, white, white, end)

print(' ' * 4, white, end, ' ' * 0, white, end,    ' ' * 5, white * 1, end, ' ' * 0, white, end)
print(' ' * 3, white, end, ' ' * 2, white, end,    ' ' * 3, white * 1, end, ' ' * 2, white, end)
print(' ' * 2, white, end, ' ' * 4, white, end,    ' ' * 1, white * 1, end, ' ' * 4, white, end)
print(' ' * 1, white, end, ' ' * 6, white, end,             white * 1, end, ' ' * 6, white, end)
print(' ' * 0, white, end, ' ' * 8, white, end,             white * 0, end, ' ' * 6, white, end)


print('\n'*2)

#Ex 3 (function y(x) = 2*x)
print('Ex 3 (function y(x) = 2*x)\n')
print('    OY')
spaces_after_OY = 12
OY_coordimates = 30
OX_coordinates = 15
spaces_before_x = 1
for i in range(20):
    while OY_coordimates >= 10:
        print(f'{OY_coordimates} ', white, end, ' ' * spaces_after_OY, white, end, spaces_before_x * ' ', f'(x = {OX_coordinates})')
        spaces_after_OY -= 1
        OY_coordimates -= 2
        OX_coordinates -= 1
        spaces_before_x += 1
    while 4 < OY_coordimates < 10:
        print(f'{OY_coordimates}  ', white, end, ' ' * spaces_after_OY, white, end, spaces_before_x * ' ', f'(x = {OX_coordinates})')
        spaces_after_OY -= 1
        OY_coordimates -= 2
        OX_coordinates -= 1
        spaces_before_x += 1


print('\n'*2)

#Ex 4 (diagram)
print('Ex 4 (diagram)')
f = open('sequence.txt', encoding = "utf-8")
data = [abs(float(x)) for x in f]
sum_chet_pos, sum_nechet_pos = 0, 0
for i in range(len(data)):
    if (i+1) % 2 == 0:
        sum_chet_pos += data[i]
    else:
        sum_nechet_pos += data[i]
sum_all = sum(data)
persent_ratio_chet = sum_chet_pos * 100 / sum_all
persent_ratio_nechet = sum_nechet_pos * 100 / sum_all
a, b = round(persent_ratio_chet, 2), round(persent_ratio_nechet, 2)

print(f'Чётные числа: {a}          Нечётные числа: {b}')
if a > b:
    for i in range(max((a - b) / 10, 1)):
        print(white, ' ', end)
    for i in range(10 - max((a - b) / 10, 1)):
        print(white, ' ', end, ' ' * 24, white, ' ', end)
else:
    for i in range(max((b - a) / 10, 1)):
        print(' ' * 28, white, ' ', end)
    for i in range(10 - max((b - a) / 10, 1)):
        print(white, ' ', end, ' ' * 24, white, ' ', end)