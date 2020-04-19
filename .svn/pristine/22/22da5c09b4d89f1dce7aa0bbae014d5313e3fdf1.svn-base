
import numpy as np


class CapaConstraint(object):

    def __init__(self):
        """
        생성자 :
        """
        # Private
        self._current_capa: float = 0.0
        self._total_capa: float = 0.0

    def init(self, total_capa: float):

        total_capa = \
            np.Inf if total_capa is None else \
            total_capa

        self._total_capa = total_capa
        self._current_capa = total_capa

    def minus_capa(self, qty: float):
        self._current_capa -= qty

    def plus_capa(self, qty: float):
        self._current_capa += qty

    def check(self, qty: float):
        if qty < self._current_capa:
            return True
        return False
