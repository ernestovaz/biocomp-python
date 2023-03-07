from biocomp.sequence_alignment import needleman_wunsch
from biocomp.phylogenetics import DistanceMatrix, neighbor_joining_tree


def read_from_file(file_path, starting_index, ending_index):
    with open(file_path, 'r') as file:
        content = file.read().replace('\n', '')
        return content[starting_index: ending_index]


if __name__ == '__main__':
    matrix = DistanceMatrix()
    matrix.insert_units(['seq_1', 'seq_2', 'seq_3', 'seq_4', 'seq_5', 'seq_6', 'seq_7', 'seq_8', 'seq_9', 'seq_10'])

    sequences = {}
    sequences['seq_1'] = read_from_file('data/seq_1.fna', 9482, 9732)
    sequences['seq_2'] = read_from_file('data/seq_2.fna', 177903, 178153)
    sequences['seq_3'] = read_from_file('data/seq_3.fna', 3519919, 3520169)
    sequences['seq_4'] = read_from_file('data/seq_4.fna', 1490249, 1490499)
    sequences['seq_5'] = read_from_file('data/seq_5.fna', 731123, 731373)
    sequences['seq_6'] = read_from_file('data/seq_6.fna', 682942, 683192)
    sequences['seq_7'] = read_from_file('data/seq_7.fna', 454284, 454434)
    sequences['seq_8'] = read_from_file('data/seq_8.fna', 15079, 15329)
    sequences['seq_9'] = read_from_file('data/seq_9.fna', 234103, 234353)
    sequences['seq_10'] = read_from_file('data/seq_10.fna', 253, 503)

    # for key, item in sequences.items():
    #     print(key, item)

    for a in sequences:
        for b in sequences:
            if a != b:
                seq_a = sequences[a]
                seq_b = sequences[b]
                aligned_a, aligned_b, distance, identity = needleman_wunsch(seq_a, seq_b, +1, -2, -2)
                matrix.set_distance(a, b, distance)
                # print(str(a) + ' vs ' + str(b) + ':' + str(distance))

    print(matrix)
    result = neighbor_joining_tree(matrix)
    #for key, value in result.items():
        #print(value)
