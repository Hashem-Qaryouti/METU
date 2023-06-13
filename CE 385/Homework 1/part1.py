import matplotlib.pyplot as plt

def even_odd_parts(x, si):
    even = []
    odd = []
    l = len(x)
    for i in range(si, si + l):
        if i % 2 == 0:
            even_val = (x[i] + x[-i]) / 2 if i <= l - i else x[i]
            even.append(even_val)
            odd_val = (x[i] - x[-i]) / 2 if i <= l - i else 0
            odd.append(odd_val)
        else:
            even_val = (x[i] + x[-i]) / 2 if i <= l - i else 0
            even.append(even_val)
            odd_val = (x[i] - x[-i]) / 2 if i <= l - i else x[i]
            odd.append(odd_val)
    plt.stem(even, linefmt='b-', markerfmt='bo', basefmt='k-')
    plt.stem(odd, linefmt='r-', markerfmt='ro', basefmt='k-')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.show()
filename = 'D:\Computer Engineering\GJU Years\Years\Third Year\Exchange Semester at METU\Signals and Systems\Homeworks\Homework 1/chirp_part_a.csv'
with open(filename, 'r') as f:
    data = f.read().split(',')
si = int(data[0])
x = [float(val) for val in data[1:]]

even_odd_parts(x, si)
