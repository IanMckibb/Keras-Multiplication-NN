import random

file_name = 'data_test.txt'
iter_count = 100

f = open(file_name, 'w')
for n in range(iter_count):
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    y = int(x1 * x2 > 50)
    f.write(str(x1) + ' ' + str(x2) + ' ' + str(y))
    if n != iter_count - 1:
        f.write('\n')