# Day 6: Tuning Trouble


def read_file(file="day6.in"):
    with open(file=file) as transmission:
        line = transmission.read().split()[0]
    return line


def detector(transmission_line, begin=0, buffer_len=4):

    buffer = [None for __ in range(buffer_len)]

    for id, character in enumerate(line):
        buffer[id % buffer_len] = character

        no_duplicates = len(buffer) == len(set(buffer)) and id >= buffer_len

        if no_duplicates:
            return id + 1


if __name__ == "__main__":
    line = read_file()

    sop = detector(line)
    som = detector(line, begin=sop - 4, buffer_len=14)

    print(f"sop: {sop}, som: {som}")
