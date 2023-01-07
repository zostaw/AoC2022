def read_file(file_name="day2.in"):
    column_a = []
    column_b = []
    with open(file=file_name) as file:
        for line in file:
            column_a.append(line[0])
            column_b.append(line[2])
    return column_a, column_b


def calculate_round(opponent_move, my_expected_result):

    if opponent_move not in ("A", "B", "C"):
        raise ValueError(
            f"opponent_move is not legal. It is {opponent_move}, while it should be one of A, B, C (str)."
        )
    if my_expected_result not in ("X", "Y", "Z"):
        raise ValueError(
            f"my_expected_result is not legal. It is {my_expected_result}, while it should be one of X, Y, Z (str)."
        )

    # matrix of possible results,
    # row - result dependent on expected result
    # column - result dependent on opponent's move
    results_matrix = [[3, 1, 2], [4, 5, 6], [8, 9, 7]]

    # transform ascii into matrix id
    # X -> id 0
    my_expected_result = ord(my_expected_result) - 88
    # A -> id 0
    opponent_move = ord(opponent_move) - 65

    result = results_matrix[my_expected_result][opponent_move]

    return result


def calculate_score(opponent_moves, my_expected_results):
    my_score = 0
    for opponent_move, my_expected_result in zip(opponent_moves, my_expected_results):
        my_score += calculate_round(opponent_move, my_expected_result)

    return my_score


if __name__ == "__main__":
    opponent_moves, my_expected_results = read_file("day2.in")
    result = calculate_score(opponent_moves, my_expected_results)

    print(f"My result: {result}.")
