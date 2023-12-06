import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + 2*x + 1

x = np.linspace(-5, 5, 100)
y = f(x)

plt.plot(x, y)
plt.title('f(x) = x^3 + 2x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
