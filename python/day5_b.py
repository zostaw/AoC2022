def day5():
    cargo, rules = parse_input()
    calculate_cargo_movements(cargo, rules)


def parse_input(file="day5.in"):

    with open(file) as file:
        for ln, line in enumerate(file):

            if ln == 0:
                stacks_len = len(line)
                cargo = [[] for __ in range(int(stacks_len / 4))]
                rules = []
                cargo_section = True

            # data separator
            if line == "\n":
                cargo_section = False
                continue

            if cargo_section:
                # information is stored every 4 chars
                for stack_id, crate in enumerate(line[1:stacks_len:4]):
                    if crate != " ":
                        cargo[stack_id].insert(0, crate)
            else:
                # parse and append dict
                _move = line.split()[1]
                _from = line.split()[3]
                _to = line.split()[5]
                rules.append({"move": _move, "from": _from, "to": _to})

    return cargo, rules


def calculate_cargo_movements(cargo, rules):
    for rule in rules:
        moves_nb = int(rule["move"])
        # stacks are numbered from 1, but list starts with 0
        from_id = int(rule["from"]) - 1
        to_id = int(rule["to"]) - 1

        moved_stack = []
        for move in range(moves_nb):
            moved_stack.insert(0, cargo[from_id].pop())
        cargo[to_id] += moved_stack

    result = ""
    for stack in cargo:
        result += stack[-1]

    print(result)


if __name__ == "__main__":
    day5()
