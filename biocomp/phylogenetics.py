import numpy as np
from .genetic_tree import TreeNode


class DistanceMatrix:
    def __init__(self):
        self.matrix = {}

    def get_size(self):
        return len(self.matrix)

    def insert_unit(self, unit_name):
        self.matrix[unit_name] = {}
        self.matrix[unit_name][unit_name] = 0.0

    def insert_units(self, unit_list):
        for unit in unit_list:
            self.insert_unit(unit)

    def remove_unit(self, unit_name):
        self.matrix.pop(unit_name, None)
        for key, unit in self.matrix.items():
            unit.pop(unit_name, None)

    def get_units(self):
        return list(self.matrix.keys())

    def set_distance(self, u1, u2, distance):
        self.matrix[u1][u2] = distance
        self.matrix[u2][u1] = distance

    def get_distance(self, u1, u2):
        return self.matrix[u1][u2]

    def get_smallest_distance(self):
        smallest = None
        pair = None
        for unit in self.matrix:
            for other_unit, distance in self.matrix[unit].items():
                if unit != other_unit and (smallest is None or distance < smallest):
                    smallest = distance
                    pair = (unit, other_unit)

        return smallest, pair

    def get_total_distance(self, unit):
        return sum(self.matrix[unit].values())

    def get_net_divergence(self, a, b):
        distance_between = self.get_distance(a, b)
        total_a = self.get_total_distance(a)
        total_b = self.get_total_distance(b)
        n = max(1, self.get_size() - 2)
        return distance_between - (total_a / n) - (total_b / n)

    def get_lowest_net_divergence(self, useScoring=False):
        lowest = None
        pair = None
        for unit in self.matrix:
            for other_unit in self.matrix[unit]:
                if unit != other_unit:
                    divergence = (self.get_net_divergence(unit, other_unit))
                    if lowest is None or (not useScoring and divergence < lowest) or (useScoring and divergence > lowest):
                        lowest = divergence
                        pair = (unit, other_unit)

        return lowest, pair

    def __str__(self):
        data = [[self.matrix[u1][u2] for u2 in self.matrix]
                for u1 in self.matrix]
        return str(np.array(data))


def upmga_tree(matrix):
    tree_branches = {}

    while matrix.get_size() > 1:

        distance, (a, b) = matrix.get_smallest_distance()

        branch_a = tree_branches.pop(a, TreeNode(a))
        branch_b = tree_branches.pop(b, TreeNode(b))

        branch_a.set_length(distance / 2)
        branch_b.set_length(distance / 2)

        middle_branch = TreeNode()
        middle_branch.add_children([branch_a, branch_b])

        a_b = "".join([a, b])
        tree_branches[a_b] = middle_branch

        other_units = [x for x in matrix.get_units() if x not in [a, b]]

        matrix.insert_unit(a_b)
        for unit in other_units:
            dist_a = matrix.get_distance(unit, a)
            dist_b = matrix.get_distance(unit, b)
            matrix.set_distance(a_b, unit, (dist_a + dist_b) / 2)

        matrix.remove_unit(a)
        matrix.remove_unit(b)

    return tree_branches


def neighbor_joining_tree(matrix, useScoring=False):
    tree_branches = {}

    while matrix.get_size() > 1:

        divergence, (a, b) = matrix.get_lowest_net_divergence(useScoring)

        distance_ab = matrix.get_distance(a, b)
        total_a = matrix.get_total_distance(a) / max(1, matrix.get_size() - 2)
        total_b = matrix.get_total_distance(b) / max(1, matrix.get_size() - 2)

        branch_a = tree_branches.pop(a, TreeNode(a))
        branch_b = tree_branches.pop(b, TreeNode(b))

        branch_a.set_length(distance_ab / 2 + (total_a - total_b) / 2)
        branch_b.set_length(distance_ab / 2 + (total_b - total_a) / 2)

        middle_branch = TreeNode()
        middle_branch.add_children([branch_a, branch_b])

        a_b = "".join([a, b])
        tree_branches[a_b] = middle_branch

        other_units = [x for x in matrix.get_units() if x not in [a, b]]

        matrix.insert_unit(a_b)
        for unit in other_units:
            dist_to_a = matrix.get_distance(unit, a)
            dist_to_b = matrix.get_distance(unit, b)
            matrix.set_distance(a_b, unit, (dist_to_a + dist_to_b - distance_ab) / 2)

        matrix.remove_unit(a)
        matrix.remove_unit(b)

    return tree_branches


def upmga_test():
    matrix = DistanceMatrix()

    matrix.insert_units(['a', 'b', 'c', 'd', 'e', 'f'])
    matrix.set_distance('a', 'b', 2)
    matrix.set_distance('c', 'a', 4)
    matrix.set_distance('c', 'b', 4)
    matrix.set_distance('d', 'a', 6)
    matrix.set_distance('d', 'b', 6)
    matrix.set_distance('d', 'c', 6)
    matrix.set_distance('e', 'a', 6)
    matrix.set_distance('e', 'b', 6)
    matrix.set_distance('e', 'c', 6)
    matrix.set_distance('e', 'd', 4)
    matrix.set_distance('f', 'a', 8)
    matrix.set_distance('f', 'b', 8)
    matrix.set_distance('f', 'c', 8)
    matrix.set_distance('f', 'd', 8)
    matrix.set_distance('f', 'e', 8)

    print(matrix)
    print()

    result = upmga_tree(matrix)
    for key, value in result.items():
        print(value)


def neighbor_joining_test():
    matrix = DistanceMatrix()

    matrix.insert_units(['a', 'b', 'c', 'd'])
    matrix.set_distance('b', 'a', 4)
    matrix.set_distance('c', 'a', 5)
    matrix.set_distance('c', 'b', 7)
    matrix.set_distance('d', 'a', 10)
    matrix.set_distance('d', 'b', 12)
    matrix.set_distance('d', 'c', 9)

    print(matrix)
    print()

    result = neighbor_joining_tree(matrix)
    for key, value in result.items():
        print(value)


if __name__ == '__main__':
    neighbor_joining_test()
