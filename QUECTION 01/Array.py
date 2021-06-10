import numpy as np


class stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = np.array([])
