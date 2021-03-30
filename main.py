import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import constants



def frange(begin, end, step):
    res = []
    current = begin
    while current <= end:
        res.append(current)
        current += step
    return res


def draw_axe(plot, ln):
    plot.plot([i for i in range(ln)], [0 for i in range(ln)])
    plot.vlines(0, ln, 0)


class Product:
    def __init__(self,
                 name: str,
                 mid_cost: int,
                 weight: float,
                 consumption: float):
        self.name = name
        self.mid_cost = mid_cost
        self.weight = weight
        self.consumption = consumption


class Market:
    def __init__(self,
                 name: str,
                 population: int,   # количество семей
                 richness: int,     # богатство в абстрактных единицах 
                 dispersy: float):  # неравенство межжду слоями населения
        self.name = name
        self.population = population
        self.richness = richness
        self.dispersy = dispersy
        self._generate_population()

    def _generate_population(self):
        # draw_axe(plt, 5)
        # const
        k = 0.1

        # params
        lux = 1.0
        dis = 1.0
        S = 0.0
        B = 0.0

        # raw calculations
        B = B * constants.richness_inf
        S *= 0.5
        dis *= 2
        K = dis/lux
        x = [i for i in frange(-0.1, 4.1, 0.2)]
        y = [K/(i + K*k - S) - K*k + B + S for i in x]

        # plt.plot(x, y)

        spl = UnivariateSpline(x, y)
        spl.set_smoothing_factor(0.1)
        x = [i for i in frange(-0.1, 4.1, 0.001)]

        plt.plot(x, spl(x))


        # params
        lux = 1.0
        dis = 1.0
        S = 0
        B = 0.0
        t = 2

        # raw calculations
        B = B * constants.richness_inf
        S *= 0.5
        dis *= 2
        K = dis/lux
        x = [i for i in frange(-0.1, 4.1, 0.2)]
        y = [(K/(i + K*k - S) - K*k + B + S)*t for i in x]

        # plt.plot(x, y)

        spl = UnivariateSpline(x, y)
        spl.set_smoothing_factor(0.1)
        x = [i for i in frange(-0.1, 4.1, 0.001)]

        plt.plot(x, spl(x), color="red")
        plt.show()


class LocalMarket:
    def __init__(self, prod, consumers):
        self.prod = prod
        self.consumers = consumers

    def draw(self):
        # axes
        pass





market = Market("Мухосранск", 1500, 50, 0.5)