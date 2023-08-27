import string


def priority(elem):
    if elem in (string.ascii_lowercase):
        return ord(elem) - 96
    elif elem in (string.ascii_uppercase):
        return ord(elem) - 38
    else:
        return None


def get_priorities_total():
    result = 0
    with open(file="day3.in") as file:
        for line in file:
            middle = int((len(line) - 1) / 2)
            A = line[0:middle]
            B = line[middle : int(len(line) - 1)]

            for elem in set(A).intersection(B):
                result += priority(elem)

        return result


if __name__ == "__main__":
    result = get_priorities_total()
    print(result)
