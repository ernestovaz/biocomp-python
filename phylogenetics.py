import numpy as np


# Matrix class to be used in the neighbor-joining algorithm
class NJMatrix:
    def __init__(self):
        self.matrix = {}

    def insert_unit(self, unit_name):
        self.matrix[unit_name] = {}
        self.matrix[unit_name][unit_name] = 0.0

    def insert_units(self, unit_list):
        for unit in unit_list:
            self.insert_unit(unit)

    def remove_unit(self, unit_name):
        del self.matrix[unit_name]
        for key, unit in self.matrix:
            unit.pop(unit_name, None)

    def add_distance(self, u1, u2, distance):
        self.matrix[u1][u2] = distance
        self.matrix[u2][u1] = distance

    def get_distance(self, u1, u2):
        return self.matrix[u1][u2]

    def __str__(self):
        data = [[self.matrix[u1][u2] for u2 in self.matrix]
                for u1 in self.matrix]
        return str(np.array(data))
