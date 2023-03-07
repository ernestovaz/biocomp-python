from biocomp.phylogenetics import DistanceMatrix, neighbor_joining_tree


def construct_matrix():
    matrix = DistanceMatrix()

    matrix.insert_units(['A', 'B', 'C', 'D', 'E', 'F'])
    matrix.set_distance('B', 'A', 1.4230670)
    matrix.set_distance('C', 'A', 1.2464736)
    matrix.set_distance('D', 'A', 2.4829678)
    matrix.set_distance('E', 'A', 1.6023069)
    matrix.set_distance('F', 'A', 0.7448415)
    matrix.set_distance('C', 'B', 1.8985344)
    matrix.set_distance('D', 'B', 3.1350286)
    matrix.set_distance('E', 'B', 2.2543677)
    matrix.set_distance('F', 'B', 1.9430337)
    matrix.set_distance('D', 'C', 1.4820114)
    matrix.set_distance('E', 'C', 0.6013505)
    matrix.set_distance('F', 'C', 1.7664403)
    matrix.set_distance('E', 'D', 1.2678046)
    matrix.set_distance('F', 'D', 3.0029345)
    matrix.set_distance('F', 'E', 2.1222736)

    return matrix


if __name__ == '__main__':
    matrix = construct_matrix()
    print('Initial matrix: ')
    print(construct_matrix())
    print()
    print('Result:')

    result = neighbor_joining_tree(matrix)
    for key, value in result.items():
        print(value)
