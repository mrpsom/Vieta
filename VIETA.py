import math
i = 1

while(i >= 1):
    in1 = int(input('I will find two numbers with a sum of (insert an integer): '))
    in2 = int(input('And a product of (insert an integer): '))
    d = ((in1 ** 2) - (4 * in2))
    if d >= 0:
        print('They will be the two solutions of the quadratic equation: x^2-(', in1, 'x)+(', in2, ')=0')
        print(f'The first number will be x1={(in1 + math.sqrt((in1 ** 2)-(4 * in2))) / 2}\n')
        print(f'The second number will be x2={(in1 - math.sqrt((in1 ** 2)-(4 * in2))) / 2}')
    else:
        print('There are no such real numbers.')
    in3 = str
    while in3 != 'N' and in3!= 'Y':
        in3 = input('Try for other numbers? Y/N:')
        if in3 == 'N':
            i = 0
        elif in3 == 'Y':
            i = 1