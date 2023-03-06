import numpy as np
from genetic_tree import TreeNode


# Matrix class to be used in the neighbor-joining algorithm
class NJMatrix:
    def __init__(self):
        self.matrix = {}

    def is_empty(self):
        return (len(self.matrix) == 0)

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
        for unit, unit_dict in self.matrix.items():
            for other_unit, distance in unit_dict.items():
                if (smallest is None or distance < smallest) and unit != other_unit:
                    print(unit, other_unit)
                    smallest = distance
                    pair = (unit, other_unit)
        return smallest, pair[0], pair[1]

    def __str__(self):
        data = [[self.matrix[u1][u2] for u2 in self.matrix]
                for u1 in self.matrix]
        return str(np.array(data))


def calculate_neighbour_joining(matrix):
    tree_branches = {}

    while(not matrix.is_empty()):

        distance, a, b = matrix.get_smallest_distance()

        branch_a = tree_branches.pop(a, TreeNode(a))
        branch_b = tree_branches.pop(b, TreeNode(b))

        branch_a.set_length(distance / 2)
        branch_b.set_length(distance / 2)

        middle_branch = TreeNode()
        middle_branch.add_children([branch_a, branch_b])

        a_b = "".join([a, b])
        tree_branches[a_b] = middle_branch

        all_units = matrix.get_units()
        other_units = [x for x in all_units if x not in [a, b]]

        matrix.insert_unit(a_b)
        for unit in other_units:
            dist_a = matrix.get_distance(unit, a)
            dist_b = matrix.get_distance(unit, b)
            matrix.set_distance(a_b, unit, (dist_a + dist_b) / 2)

        matrix.remove_unit(a)
        matrix.remove_unit(b)

        print(matrix)

    return tree_branches


if __name__ == '__main__':
    matrix = NJMatrix()

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

    result = calculate_neighbour_joining(matrix)

    print(result)
