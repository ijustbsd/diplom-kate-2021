import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

x0 = 1
q = 0.5
d = 2
a = 1
T = 1

def float_pow(x, y):
    return np.sign(x) * np.abs(x) ** y

def g1(x):
    return np.sin(x) ** 2

def g2(x):
    return np.exp(x)

def g3(_):
    return 1

def ml(z, a=q, b=q):
    k = np.arange(1, 100).reshape(-1, 1)
    E = z ** k / gamma(a * k + b)
    return np.sum(E, axis=0)

def result_func(t, g):

    def f(s, t):
        ts = t - s
        return float_pow(ts, q-1) * ml((-d + a) * float_pow(ts, q)) * g(s)

    result = []
    for x in t:
        curr_result = ml(x, b=1) * x0
        if x != 0:
            curr_result += quad(f, 0, x, args=(x,))[0]
        result.append(curr_result)
    return np.array(result)

x = np.arange(0, T, 0.01)

plt.rcParams.update({'font.size': 24})

plt.plot(x, result_func(x, g1), 'r', linewidth=4, label=r'$G(s) = sin^2(s)$')
plt.plot(x, result_func(x, g2), 'g', linewidth=4, label=r'$G(s) = e^s$')
plt.plot(x, result_func(x, g3), 'b', linewidth=4,label=r'$G(s) = 1$')

plt.grid()
plt.legend(prop={'size': 20})
plt.show()
