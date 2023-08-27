def read_file(file_name="day2.in"):
    column_a = []
    column_b = []
    with open(file=file_name) as file:
        for line in file:
            column_a.append(line[0])
            column_b.append(line[2])
    return column_a, column_b


def calculate_round(opponent_move, expected_outcome):

    if opponent_move not in ("A", "B", "C"):
        raise ValueError(
            f"opponent_move is not legal. It is {opponent_move}, while it should be one of A, B, C (str)."
        )
    if expected_outcome not in ("X", "Y", "Z"):
        raise ValueError(
            f"expected_outcome is not legal. It is {expected_outcome}, while it should be one of X, Y, Z (str)."
        )

    # matrix of possible results,
    # row - result dependent on expected outcome
    # column - result dependent on opponent's move
    results_matrix = [[3, 1, 2], [4, 5, 6], [8, 9, 7]]

    # transform ascii into matrix id
    # X -> id 0
    expected_outcome = ord(expected_outcome) - 88
    # A -> id 0
    opponent_move = ord(opponent_move) - 65

    result = results_matrix[expected_outcome][opponent_move]

    return result


def calculate_score(opponent_moves, expected_outcomes):
    my_score = 0
    for opponent_move, expected_outcome in zip(opponent_moves, expected_outcomes):
        my_score += calculate_round(opponent_move, expected_outcome)

    return my_score


if __name__ == "__main__":
    opponent_moves, expected_outcomes = read_file("day2.in")
    result = calculate_score(opponent_moves, expected_outcomes)

    print(f"My result: {result}.")
