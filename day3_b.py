import string


def get_rucksacks_inventory(file):
    # returns list of lists
    # each table contains single group (three rucksacks)
    with open(file=file) as file:
        rucksacks_inventory = []

        single_group_inventory = []
        elf_counter = 0

        for line in file:
            single_group_inventory.append(line.replace("\n", ""))
            elf_counter += 1

            if elf_counter == 3:
                # close a group of 3 and add to inventory
                rucksacks_inventory.append(single_group_inventory)
                elf_counter = 0
                single_group_inventory = []

    return rucksacks_inventory


def priority(elem):
    if elem in (string.ascii_lowercase):
        return ord(elem) - 96
    elif elem in (string.ascii_uppercase):
        return ord(elem) - 38
    else:
        return None


def get_priorities_total():
    result = 0
    rucksacks_inventory = get_rucksacks_inventory("day3.in")

    for group in rucksacks_inventory:
        for elem in set(group[0]).intersection(group[1]).intersection(group[2]):
            result += priority(elem)

    return result


if __name__ == "__main__":
    result = get_priorities_total()
    print(result)
