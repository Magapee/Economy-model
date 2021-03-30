import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import constants
from Product import Product


k = 0.1  # Константа изогнутости


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


class LocalMarket:
    def __init__(self,
                 name: str,
                 population: int,   # количество семей
                 richness: int,     # богатство в абстрактных единицах 
                 dispersy: float,
                 product):  # неравенство межжду слоями населения
        self.name = name
        self.population = population
        self.richness = richness
        self.dispersy = dispersy
        self.product = product

        self._pull = self.product
        # self._generate_population()

    def generate_cost(self, quantity, raise_factor):
        B = self.richness * constants.richness_inf
        S = raise_factor
        dis = self.dispersy * 2
        K = dis/self.product.lux

        cost = lambda x: (K/((x + K*k - S*0.5) - K*k + B + S*0.5) * self.population * self.product.consumption * self.product.not_panic_time / 50)*self.product.mid_cost

        x = [i for i in frange(-0.1, 1000, 0.2)]
        y = [cost(i) for i in frange(-0.1, 1000, 0.2)]
        plt.plot(x, y)
        plt.vlines(quantity, 10, 0)
        plt.show()
        return cost(quantity)

    def _generate_population(self):
        # draw_axe(plt, 5)
        # const

        draw_axe(plt, 8)
        # params
        lux = 1.0
        dis = 1.0
        S = -0.1
        B = 0.0

        # raw calculations
        B = B * constants.richness_inf
        S *= 0.5
        dis *= 2
        K = dis/lux
        x = [i for i in frange(-0.1, 6, 0.2)]
        y = [K/(i + K*k - S*0.5) - K*k + B + S*0.5 for i in x]

        # plt.plot(x, y)

        spl = UnivariateSpline(x, y)
        spl.set_smoothing_factor(0.1)
        x = [i for i in frange(-0.1, 6, 0.001)]

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
        x = [i for i in frange(-0.1, 6, 0.2)]
        y = [(K/(i + K*k - S) - K*k + B + S)*t for i in x]

        # plt.plot(x, y)

        spl = UnivariateSpline(x, y)
        spl.set_smoothing_factor(0.1)
        x = [i for i in frange(-0.1, 6, 0.001)]

        plt.plot(x, spl(x), color="red")
        plt.show()


tovar = Product("Картофанчик", 1, 1, 5.0, 0.1, 8)
market = LocalMarket("Мухосранск", 1500, 50, 0.5, tovar)

print(market.generate_cost(7500, 50))