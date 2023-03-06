from biocomp.phylogenetics import NJMatrix


def construct_matrix():
    matrix = NJMatrix()

    matrix.insert_units(['A', 'B', 'C', 'D', 'E', 'F'])
    matrix.add_distance('B', 'A', 1.4230670)
    matrix.add_distance('C', 'A', 1.2464736)
    matrix.add_distance('D', 'A', 2.4829678)
    matrix.add_distance('E', 'A', 1.6023069)
    matrix.add_distance('F', 'A', 0.7448415)
    matrix.add_distance('C', 'B', 1.8985344)
    matrix.add_distance('D', 'B', 3.1350286)
    matrix.add_distance('E', 'B', 2.2543677)
    matrix.add_distance('F', 'B', 1.9430337)
    matrix.add_distance('D', 'C', 1.4820114)
    matrix.add_distance('E', 'C', 0.6013505)
    matrix.add_distance('F', 'C', 1.7664403)
    matrix.add_distance('E', 'D', 1.2678046)
    matrix.add_distance('F', 'D', 3.0029345)
    matrix.add_distance('F', 'E', 2.1222736)

    return matrix


def main():
    print(construct_matrix())


if __name__ == '__main__':
    main()
