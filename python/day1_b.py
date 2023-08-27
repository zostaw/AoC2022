# Day 1: Calorie Counting

# From a list, identify Elf that has a basket with highest amount of calories in total


def get_calories_by_elf():

    # open file
    with open(file="day1.in") as file:

        calories_by_elf = [0]
        elf_id = 0

        for line in file:
            # build list of calories for each elf
            if line == "\n":
                elf_id += 1
                calories_by_elf.append(0)
            else:
                calories_by_elf[elf_id] += int(line)
    return calories_by_elf


def top_three(lst):

    richest_elfs = [
        {"id": None, "value": 0},
        {"id": None, "value": 0},
        {"id": None, "value": 0},
    ]

    for id, value in enumerate(lst):

        # compare value with current richest_elf_ids order by richest_elf_ids
        if richest_elfs[0]["id"] is None or value > richest_elfs[0]["value"]:
            richest_elfs[2] = richest_elfs[1].copy()
            richest_elfs[1] = richest_elfs[0].copy()
            richest_elfs[0]["id"] = id
            richest_elfs[0]["value"] = value
        elif richest_elfs[1] is None or value > richest_elfs[1]["value"]:
            richest_elfs[2] = richest_elfs[1].copy()
            richest_elfs[1]["id"] = id
            richest_elfs[1]["value"] = value
        elif richest_elfs[2] is None or value > richest_elfs[2]["value"]:
            richest_elfs[2]["id"] = id
            richest_elfs[2]["value"] = value
        else:
            continue

    return richest_elfs


if __name__ == "__main__":
    calories_by_elf = get_calories_by_elf()
    print(calories_by_elf)
    richest_elfs = top_three(calories_by_elf)
    print(f"3 richest elfs: {richest_elfs}")

    total_sum = (
        richest_elfs[0]["value"] + richest_elfs[1]["value"] + richest_elfs[2]["value"]
    )

    print(f"Their total value: { total_sum}")
