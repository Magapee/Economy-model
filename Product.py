class Product:
    def __init__(self,
                 name: str,
                 mid_cost: int,
                 weight: float,
                 consumption: float,
                 lux: float,    # from 1.0 to 9.0
                 time: int):    # in turns
        self.name = name
        self.mid_cost = mid_cost
        self.weight = weight
        self.consumption = consumption
        self.lux = lux
        self.not_panic_time = time

    def get_cost_factor(self):
        return self.mid_cost