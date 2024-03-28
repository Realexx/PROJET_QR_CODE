import numpy as np


class SeedGenerator:
    def __init__(self, key):
        self.key = key
        self.random_state = np.random.RandomState(self.key)

    def generate_seeds(self, N, shape):
        return self.random_state.randint(0, min(shape), (N, 2))
