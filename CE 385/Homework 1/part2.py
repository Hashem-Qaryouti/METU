import matplotlib.pyplot as plt

def shifted_scaled(x, si, a, b):
    l = len(x)
    n = [i for i in range(si, si + l)]
    new_signal = []
    for i in n:
        ind = int(a*(i-si)+b)
        if 0 <= ind < l:
            new_signal.append(x[ind])

    m = len(new_signal)
    plt.stem(n[:m], new_signal)
    plt.title('Shifted and Scaled Signal')
    plt.xlabel('n')
    plt.ylabel('x[an+b]')
    plt.show()

filename = 'D:\Computer Engineering\GJU Years\Years\Third Year\Exchange Semester at METU\Signals and Systems\Homeworks\Homework 1/chirp_part_b.csv'
with open(filename, 'r') as f:
    data = f.read().split(',')
si = int(data[0])
a = int(data[1])
b = int(data[2])
x = [float(val) for val in data[3:]]

shifted_scaled(x, si, a, b)