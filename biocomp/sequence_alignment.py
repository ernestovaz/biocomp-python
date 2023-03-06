import numpy as np

ARROW_DIAGONAL = 1
ARROW_UP = 2
ARROW_LEFT = 3


def calculate_identity(sequence_a, sequence_b):
    count = 0
    for x, y in zip(sequence_a, sequence_b):
        if x == y:
            count += 1
    return count


def needleman_wunsch(sequence_a, sequence_b, match_value, mismatch_value, gap_value):
    # create matrices
    matrix_width = len(sequence_a) + 1
    matrix_height = len(sequence_b) + 1
    score_matrix = np.zeros((matrix_height, matrix_width))
    arrow_matrix = np.zeros((matrix_height, matrix_width))

    # initialize gap values
    for y in range(1, matrix_height):
        score_matrix[y][0] = gap_value * y
    for x in range(1, matrix_width):
        score_matrix[0][x] = gap_value * x

    # fill score_matrix
    for y in range(1, matrix_height):
        for x in range(1, matrix_width):
            diagonal = score_matrix[y - 1][x - 1]
            above = score_matrix[y - 1][x]
            left = score_matrix[y][x - 1]

            # fill score_matrix
            match_mismatch = mismatch_value
            if sequence_a[x - 1] == sequence_b[y - 1]:
                match_mismatch = match_value

            value_diagonal = diagonal + match_mismatch
            value_above = above + gap_value
            value_left = left + gap_value

            tuple_diagonal = (value_diagonal, diagonal)
            tuple_above = (value_above, above)
            tuple_left = (value_left, left)

            if tuple_diagonal >= tuple_above and tuple_diagonal >= tuple_left:
                score_matrix[y][x] = value_diagonal
                arrow_matrix[y][x] = ARROW_DIAGONAL
            elif tuple_above >= tuple_diagonal and tuple_above >= tuple_left:
                score_matrix[y][x] = value_above
                arrow_matrix[y][x] = ARROW_UP
            elif tuple_left >= tuple_diagonal and tuple_left >= tuple_above:
                score_matrix[y][x] = value_left
                arrow_matrix[y][x] = ARROW_LEFT

    score = score_matrix[matrix_height - 1][matrix_width - 1]

    # align sequences tracing back arrows
    aligned_a = sequence_a
    aligned_b = sequence_b

    x = matrix_width - 1
    y = matrix_height - 1
    tracing_back = True
    while tracing_back:
        if arrow_matrix[y][x] == ARROW_DIAGONAL:
            y -= 1
            x -= 1
        elif arrow_matrix[y][x] == ARROW_UP:
            aligned_a = aligned_a[:x] + '-' + aligned_a[x:]
            y -= 1
        else:
            aligned_b = aligned_b[:y] + '-' + aligned_b[y:]
            x -= 1
        if x == 0 and y == 0:
            tracing_back = False

    identity = calculate_identity(aligned_a, aligned_b)

    return aligned_a, aligned_b, score, identity


def smith_waterman(sequence_a, sequence_b, match_value, mismatch_value, gap_value):
    # create matrices
    matrix_width = len(sequence_a) + 1
    matrix_height = len(sequence_b) + 1
    score_matrix = np.zeros((matrix_height, matrix_width))
    arrow_matrix = np.zeros((matrix_height, matrix_width))

    # fill score_matrix
    for y in range(1, matrix_height):
        for x in range(1, matrix_width):
            diagonal = score_matrix[y - 1][x - 1]
            above = score_matrix[y - 1][x]
            left = score_matrix[y][x - 1]

            # fill score_matrix
            match_mismatch = mismatch_value
            if sequence_a[x - 1] == sequence_b[y - 1]:
                match_mismatch = match_value

            value_diagonal = diagonal + match_mismatch
            value_above = above + gap_value
            value_left = left + gap_value

            tuple_diagonal = (value_diagonal, diagonal)
            tuple_above = (value_above, above)
            tuple_left = (value_left, left)

            if value_diagonal > 0 and tuple_diagonal >= tuple_above and tuple_diagonal >= tuple_left:
                score_matrix[y][x] = value_diagonal
                arrow_matrix[y][x] = ARROW_DIAGONAL
            elif value_above > 0 and tuple_above >= tuple_diagonal and tuple_above >= tuple_left:
                score_matrix[y][x] = value_above
                arrow_matrix[y][x] = ARROW_UP
            elif value_left > 0 and tuple_left >= tuple_diagonal and tuple_left >= tuple_above:
                score_matrix[y][x] = value_left
                arrow_matrix[y][x] = ARROW_LEFT

    score = np.max(score_matrix)
    highest_values = np.argwhere(score_matrix == score)

    result_list = []
    for value in highest_values:
        # align sequences tracing back arrows
        aligned_a = ''
        aligned_b = ''

        x = value[1]
        y = value[0]
        tracing_back = True
        while tracing_back:
            if arrow_matrix[y][x] == ARROW_DIAGONAL:
                aligned_a = sequence_a[x - 1] + aligned_a
                aligned_b = sequence_b[y - 1] + aligned_b
                y -= 1
                x -= 1
            elif arrow_matrix[y][x] == ARROW_UP:
                aligned_a = '-' + aligned_a
                y -= 1
            elif arrow_matrix[y][x] == ARROW_LEFT:
                aligned_b = '-' + aligned_b
                x -= 1
            elif score_matrix[y][x] == 0:
                tracing_back = False

        identity = calculate_identity(aligned_a, aligned_b)
        result_list.add((aligned_a, aligned_b, score, identity))

    return result_list

# Commented now while I find a good place for this code!
#
# if __name__ == '__main__':
#    parser = argparse.ArgumentParser()
#    parser.add_argument('sequence_a_path', help='Path to file containing first sequence')
#    parser.add_argument('sequence_b_path', help='Path to file containing second sequence')
#
#    parser.add_argument('-M', '--match', type=int, default=2, help='Value for matches')
#    parser.add_argument('-m', '--mismatch', type=int, default=-2, help='Value for mismatches')
#    parser.add_argument('-g', '--gap', type=int, default=-5, help='Value for gaps')
#
#    arguments = parser.parse_args()
#
#    path_a = arguments.sequence_a_path
#    path_b = arguments.sequence_b_path
#
#    match_value = arguments.match
#    mismatch_value = arguments.mismatch
#    gap_value = arguments.gap
#
#    sequence_a = ''
#    sequence_b = ''
#
#    try:
#        with open(path_a, 'r') as file:
#            sequence_a = file.read().rstrip()
#    except FileNotFoundError:
#        print('Error: File not found for first sequence')
#
#    try:
#        with open(path_b, 'r') as file:
#            sequence_b = file.read().rstrip()
#    except FileNotFoundError:
#        print('Error: File not found for second sequence')
#
#    if sequence_a and sequence_b:
#        needleman_wunsch(
#            sequence_a, sequence_b,
#            match_value, mismatch_value, gap_value
#        )
