import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline


def frange(begin, end, step):
    res = []
    current = begin
    while current <= end:
        res.append(current)
        current += step
    return res


families = [15, 7, 5, 4, 1, 0.5, 0.3, 0.1, 0]
x = [i for i in frange(1, len(families), 1)]
plt.figure(1)


axes = 10
plt.plot([i for i in range(-axes, axes)], [0 for i in range(axes*2)])
plt.vlines(0, -axes, axes)


plt.plot(x, families)
plt.figure(2)


axes = 10
plt.plot([i for i in range(-axes, axes)], [0 for i in range(axes*2)])
plt.vlines(0, -axes, axes)


spl = UnivariateSpline(x, families)
spl.set_smoothing_factor(0.5)
x = [i for i in frange(0.01, 6, 0.01)]
plt.plot(x, spl(x))
plt.show()
