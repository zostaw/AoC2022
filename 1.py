# Day 1: Calorie Counting

# From a list, identify Elf that has a basket with highest amount of calories in total


def main():

    # open file
    with open(file="1.in") as file:

        calories_by_elf = [0]
        elf_id = 0

        for line in file:
            # build list of calories for each elf
            if line == "\n":
                elf_id += 1
                calories_by_elf.append(0)
            else:
                calories_by_elf[elf_id] += int(line)

    richest_elf = 0
    for id, calories in enumerate(calories_by_elf):
        if calories > calories_by_elf[richest_elf]:
            richest_elf = id

    return richest_elf, calories_by_elf[richest_elf]


if __name__ == "__main__":
    elf_id, calories = main()
    print(f"Richest elf: {elf_id}, handles {calories} calories!")
