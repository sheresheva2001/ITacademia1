# Написать программу которая находит ближайшую степень двойки к
# введенному числу. 10(8), 20(16), 1(1), 13(16)

a = 13
print(2 ** (a.bit_length() - 1))