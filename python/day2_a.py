def read_file(file_name="day2.in"):
    column_a = []
    column_b = []
    with open(file=file_name) as file:
        for line in file:
            column_a.append(line[0])
            column_b.append(line[2])
    return column_a, column_b


def calculate_round(opponent_move, my_move):

    if opponent_move not in ("A", "B", "C"):
        raise ValueError(
            f"Opponent move is not legal. It is {opponent_move}, while it should be one of A, B, C (str)."
        )
    if my_move not in ("X", "Y", "Z"):
        raise ValueError(
            f"My move is not legal. It is {my_move}, while it should be one of X, Y, Z (str)."
        )

    # points for move
    if my_move == "X":
        result = 1
    elif my_move == "Y":
        result = 2
    elif my_move == "Z":
        result = 3

    # points for result
    # A is ascii 65, X is ascii 88
    if ord(opponent_move) + 23 == ord(my_move):
        result += 3
    # 14 is win with Y or Z, 11 is for win with X
    elif ord(my_move) - ord(opponent_move) in (24, 21):
        result += 6

    return result


def calculate_score(opponent_moves, my_moves):
    my_score = 0
    for opponent_move, my_move in zip(opponent_moves, my_moves):
        my_score += calculate_round(opponent_move, my_move)

    return my_score


if __name__ == "__main__":
    opponent_moves, my_moves = read_file("day2.in")
    result = calculate_score(opponent_moves, my_moves)

    print(f"My result: {result}.")
