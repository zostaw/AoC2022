# Day 6: Tuning Trouble


def day6():
    with open(file="day6.in") as transmission:

        line = transmission.read().split()[0]
        four_buffer = [None for __ in range(4)]

        for id, character in enumerate(line):
            four_buffer[id % 4] = character

            no_duplicates = len(four_buffer) == len(set(four_buffer)) and id > 2

            if no_duplicates:
                return id + 1


if __name__ == "__main__":
    print(day6())
