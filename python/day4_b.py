import re


def extract_pairs_of_sections(file):
    # returns list of lists containing pairs of sections, ie.: [first_pair, second_pair, ...]
    # each pair on its own is a list of lists, ie.: first_pair = [[0:4][5:9]]
    list_of_pairs = []
    with open(file=file) as file:
        for line in file:

            # cut line into two ranges
            rangeA = re.sub(",.*", "", line.replace("\n", ""))
            rangeB = re.sub(".*,", "", line.replace("\n", ""))

            # transform format of a-b into list [a:b+1] for both ranges
            listA = [
                *range(
                    int(re.sub("-.*", "", rangeA)), int(re.sub(".*-", "", rangeA)) + 1
                )
            ]
            listB = [
                *range(
                    int(re.sub("-.*", "", rangeB)), int(re.sub(".*-", "", rangeB)) + 1
                )
            ]

            list_of_pairs.append([listA, listB])

    return list_of_pairs


def is_overlapping(pair):
    # returns true value if one pair contains the other or otherwise
    # takes list of list as argument: [[list1], [list2]]

    if set(pair[0]).intersection(pair[1]):
        return True
    else:
        return False


def count_overlapped_sections():

    result = 0
    for pair in extract_pairs_of_sections("day4.in"):
        result += is_overlapping(pair)

    return result


if __name__ == "__main__":

    result = count_overlapped_sections()
    print(result)
