# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4)

def maximumdivisor(n):
    return (n & (~(n - 1)))

if __name__ == '__main__':
    n = 5
    print(maximumdivisor(n))

