import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# (a) 
def compute_fourier_coeffs(signal, T, n):
    N = len(signal)
    t = np.array([(-T/2) + (i * T/N) for i in range(N)])
    coeffs = []
    
    # DC component equal to the average value of the signal over a period
    a_0 = np.sum(signal)/N
    coeffs.append(a_0)
    
    # cosine and sine coefficients
    for k in range(1, n+1):
        cos_terms = signal * np.cos(2*np.pi*k*t/T)
        sin_terms = signal * np.sin(2*np.pi*k*t/T)
        
        a_k = np.sum(cos_terms)/N 
        b_k = np.sum(sin_terms)/N 
        
        coeffs.append((a_k, b_k))

    return coeffs

# (b) 
def approx_fourier(coeffs, T, n, N):
    t = np.array([(-T/2) + (i * T/N) for i in range(N)])
    approx = np.zeros(N) + coeffs[0]
    
    # add cosine and sine terms for each coefficient
    for k in range(1, n+1):
        a_k, b_k = coeffs[k]
        cos_terms = a_k * np.cos(2*np.pi*k*t/T)
        sin_terms = b_k * np.sin(2*np.pi*k*t/T)
        
        approx += cos_terms + sin_terms
    return approx

# (c)
N = 1000
T = 1
t_arr = np.array([(-T/2) + (i * T) for i in range(N)])
s = np.array([1 if i < N/2 else -1 for i in range(N)])
for n in [1, 5, 10, 50, 100]:
    coeffs = compute_fourier_coeffs(s, T, n)
    approx = approx_fourier(coeffs, T, n, N)
    plt.plot(t_arr, s, label='Original')
    plt.plot(t_arr, approx, label=f'Approximation (n={n})')
    plt.title(f'Fourier Series Approximation of Square Wave with n={n}')
    plt.legend()
    plt.show()

# (d) 
sawtooth_wave = signal.sawtooth(2 * np.pi * t_arr)
for n in [1, 5, 10, 50, 100]:
    coeffs = compute_fourier_coeffs(sawtooth_wave, T, n)
    approx = approx_fourier(coeffs, T, n, N)
    plt.plot(t_arr, sawtooth_wave, label='Original')
    plt.plot(t_arr, approx, label=f'Approximation (n={n})')
    plt.title(f'Fourier Series Approximation of Sawtooth Wave with n={n}')
    plt.legend()
    plt.show()

# When we increase the number of Fourier series coefficients, 
# the approximation becomes more accurate, and the reconstructed 
# signal will be closer to the original signal. 
