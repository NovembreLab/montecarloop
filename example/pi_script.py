#!/usr/bin/python3

from pathlib import Path
import numpy as np

from montecarloop import Dealer, JsonFileCache

class PiEstimator:
    def __init__(self, sim_params):
        self.n = int(sim_params["n"])
        self.r = float(sim_params["r"])

    def simulate(self, seed):
        rng = np.random.default_rng(seed)
        # generate random (x,y) points in square [-1,1)x[-1,1)
        x = rng.random(self.n) * 2 - 1
        y = rng.random(self.n) * 2 - 1
        inside_circle = x**2 + y**2 < self.r**2
        area = 4 * np.sum(inside_circle) / self.n
        return dict(pi=(area / self.r**2))


if __name__ == "__main__":
    dest = Path(__file__).with_name("cache.json")
    seconds = 60 * 60
    Dealer.handle_keyboard_interrupts()
    Dealer(JsonFileCache(dest), PiEstimator).run(seconds)
    print("Done.")

