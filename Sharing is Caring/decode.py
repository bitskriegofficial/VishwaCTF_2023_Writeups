data = [
    [[(1, 76), (2, 31), (3, 58), (4, 50), (5, 7)], 107],
    [[(1, 9), (2, 146), (3, 170), (4, 81), (5, 52)], 173],
    [[(1, 48), (2, 102), (3, 86), (4, 0), (5, 35)], 191],
    [[(1, 12), (2, 44), (3, 1), (4, 82), (5, 88)], 199],
    [[(1, 50), (2, 103), (3, 51), (4, 121), (5, 86)], 227],
    [[(1, 13), (2, 110), (3, 74), (4, 62), (5, 74)], 157],
    [[(1, 56), (2, 6), (3, 44), (4, 43), (5, 3)], 127],
    [[(1, 148), (2, 123), (3, 9), (4, 104), (5, 110)], 149],
    [[(1, 77), (2, 85), (3, 94), (4, 104), (5, 115)], 127],
    [[(1, 235), (2, 20), (3, 195), (4, 43), (5, 42)], 239],
    [[(1, 118), (2, 138), (3, 168), (4, 208), (5, 47)], 211],
    [[(1, 36), (2, 81), (3, 90), (4, 63), (5, 0)], 97],
    [[(1, 128), (2, 19), (3, 50), (4, 84), (5, 121)], 137],
    [[(1, 106), (2, 138), (3, 31), (4, 143), (5, 116)], 179],
    [[(1, 91), (2, 18), (3, 27), (4, 21), (5, 0)], 97],
    [[(1, 116), (2, 98), (3, 56), (4, 121), (5, 31)], 131],
    [[(1, 17), (2, 48), (3, 69), (4, 80), (5, 81)], 127],
    [[(1, 36), (2, 36), (3, 51), (4, 20), (5, 4)], 61],
    [[(1, 88), (2, 84), (3, 83), (4, 85), (5, 90)], 127],
    [[(1, 104), (2, 84), (3, 42), (4, 85), (5, 106)], 107],
    [[(1, 50), (2, 68), (3, 13), (4, 63), (5, 40)], 89],
    [[(1, 60), (2, 105), (3, 122), (4, 111), (5, 72)], 127],
    [[(1, 61), (2, 119), (3, 112), (4, 40), (5, 60)], 157],
    [[(1, 92), (2, 0), (3, 63), (4, 58), (5, 208)], 223],
    [[(1, 151), (2, 80), (3, 48), (4, 55), (5, 101)], 157],
    [[(1, 12), (2, 10), (3, 45), (4, 58), (5, 49)], 59],
    [[(1, 133), (2, 104), (3, 8), (4, 119), (5, 26)], 137],
    [[(1, 14), (2, 24), (3, 149), (4, 7), (5, 171)], 191],
    [[(1, 12), (2, 54), (3, 86), (4, 19), (5, 31)], 89],
    [[(1, 9), (2, 70), (3, 82), (4, 45), (5, 170)], 211],
    [[(1, 33), (2, 35), (3, 2), (4, 8), (5, 16)], 37],
    [[(1, 13), (2, 204), (3, 65), (4, 18), (5, 63)], 211],
]

for i in data:
    for x in range(0,127):
        for a in range(1,i[1]):
            for b in range(1,i[1]):
                if(i[0][0][1] == ((x + a + b)%i[1]) and i[0][1][1] == ((x + 2*a +4*b)%i[1]) and i[0][2][1] == ((x + 3*a +9*b)%i[1]) and i[0][3][1] == ((x + 4*a +16*b)%i[1]) and i[0][4][1] == ((x + 5*a +25*b)%i[1])):
                    print("{%d},{%d},{%d}" %(x,a,b),sep=",")
    print("-")