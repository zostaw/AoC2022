import numpy as np


def load_file(file_name):

    with open(file=file_name) as file:
        vect = []
        for line in file:
            line_vect = line.replace("\n", "")
            vect.append([eval(__) for __ in list(line_vect)])

    return vect


def search_single_dim(vect):
    rows = len(vect)
    cols = len(vect[0])

    visible_trees = [[0 for __ in range(cols)] for __ in range(rows)]

    # find peaks x, mark one side
    for row_id in range(rows):
        # first is always visible and always hides lower trees
        visible_trees[row_id][0] = 1
        max_left = vect[row_id][0]

        for col_id in range(1, cols):
            # stop if max is 9
            if max_left == 9:
                break

            value = vect[row_id][col_id]
            if value > max_left:
                max_left = value
                visible_trees[row_id][col_id] = 1

        # the other side
        visible_trees[row_id][-1] = 1
        max_right = vect[row_id][-1]

        # one does not need to search from the other side if first element is peak value
        if max_right == max_left:
            continue

        right_id = 2
        while max_right < max_left:
            value = vect[row_id][-right_id]
            if value == max_left:
                # first found peak is visible, but no more
                visible_trees[row_id][-right_id] = 1
                break

            if value > max_right:
                visible_trees[row_id][-right_id] = 1
                max_right = value

            right_id += 1

    return visible_trees


def find_visible(matrx):

    vect = np.array(matrx)
    rows = len(vect)
    cols = len(vect[0])

    transposed_vect = np.transpose(vect)
    trans_rows = len(transposed_vect)
    trans_cols = len(transposed_vect[0])

    visible_total = 0

    searched_x = search_single_dim(vect)
    searched_y = np.transpose(search_single_dim(np.transpose(vect)))

    final_vec = searched_x + searched_y

    for row in range(rows):
        for col in range(cols):
            if final_vec[row][col]:
                visible_total += 1

    return visible_total


if __name__ == "__main__":
    matrx = load_file("day8.in")
    print(f"Visible trees: {find_visible(matrx)}")
