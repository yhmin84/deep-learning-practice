import numpy as np


class SGD:
    def __init__(self, learning_rate=0.01):
        self._learning_rate = learning_rate

    def update(self, params: dict, grads: dict):
        for key in params.keys():
            params[key] -= self._learning_rate * grads[key]


class Momentum:
    def __init__(self, learning_rate=0.01, momentum=0.9):
        self._learning_rate = learning_rate
        self._momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self._momentum * self.v[key] - self._learning_rate * grads[key]
            params[key] += self.v[key]


class AdaGrad:
    def __init__(self, learning_rate=0.01):
        self._learning_rate = learning_rate
        self._h = None

    def update(self, params: dict, grads: dict):
        if self._h is None:
            self._h = {}
            for key, val in params.items():
                self._h[key] = np.zeros_like(val)

        for key in params.keys():
            self._h[key] += grads[key] * grads[key]
            params[key] -= self._learning_rate * grads[key] / (np.sqrt(self._h[key]) + 1e-7)




