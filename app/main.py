import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

x0 = 1
q = 0.5
d = 2
a = 1
t = 1

def float_pow(x, y):
    return np.sign(x) * np.abs(x) ** y

def g(x):
    return np.sin(x) ** 2

def ml(z, a=q, b=q):
    k = np.arange(100).reshape(-1, 1)
    E = z ** k / gamma(a * k + b)
    return np.sum(E, axis=0)

def result_func(t):

    def f(s, t):
        ts = t - s
        return float_pow(ts, q-1) * ml((-d + a) * float_pow(ts, q)) * g(s)

    result = []
    for x in t:
        result.append(ml(x) * x0 + quad(f, 0, 1, args=(x,))[0])
    return np.array(result)

x = np.arange(-1, 1, 0.05)

plt.plot(x, ml(x), label='ml')
plt.plot(x, g(x), label='sin^2')
plt.plot(x, ml(x) * g(x), label='ml * sin^2')
plt.plot(x, result_func(x), label='result_func')

plt.grid()
plt.legend()
plt.show()
