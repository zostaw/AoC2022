import numpy as np


def load_file(file_name):

    with open(file=file_name) as file:
        vect = []
        for line in file:
            line_vect = line.replace("\n", "")
            vect.append([eval(__) for __ in list(line_vect)])

    return vect


def scenic_score(vect, row_id, col_id):

    node_value = vect[row_id][col_id]
    # check 4 directions
    score_up = 0
    score_right = 0
    score_down = 0
    score_left = 0
    limit_up = 0
    limit_right = len(vect[0]) - 1
    limit_down = len(vect) - 1
    limit_left = 0

    # check direction
    distance = 1
    while row_id - distance >= limit_up:
        score_up = distance
        if vect[row_id - distance][col_id] >= node_value:
            break
        distance += 1

    distance = 1
    while col_id + distance <= limit_right:
        score_right = distance
        if vect[row_id][col_id + distance] >= node_value:
            break
        distance += 1

    distance = 1
    while row_id + distance <= limit_down:
        score_down = distance
        if vect[row_id + distance][col_id] >= node_value:
            break
        distance += 1

    distance = 1
    while col_id - distance >= limit_left:
        score_left = distance
        if vect[row_id][col_id - distance] >= node_value:
            break
        distance += 1

    # print(f"up/right/down/left: {score_up}/{score_right}/{score_down}/{score_left}")

    return score_up * score_right * score_down * score_left


def best_scenic_score(matrx):

    vect = np.array(matrx)
    rows = len(vect)
    cols = len(vect[0])

    top_score = 0
    top_row_id = 0
    top_col_id = 0
    peak_vector = []

    for row_id in range(1, rows - 1):
        for col_id in range(1, cols - 1):
            score = scenic_score(vect, row_id, col_id)
            if score > top_score:
                top_score = score
                top_row_id = row_id
                top_col_id = col_id

    return top_score


if __name__ == "__main__":
    matrx = load_file("day8.in")
    print(f"Top score: {best_scenic_score(matrx)}")
