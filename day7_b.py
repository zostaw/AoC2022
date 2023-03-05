# Day 7: No Space Left On Device


def read_file(file):

    terminal_output = []
    with open(file=file) as file:
        for line in file:
            terminal_output.append(line.replace("\n", ""))

    return terminal_output


class Node:
    def __init__(self, name=None, file_type="dir", size=0, parent=None):
        # parent - Node object
        # name - string
        # file_type - dir/file
        # size - for files, for dirs add_size method is keeping track of it

        # verify types
        allowed_types = ["dir", "file"]
        if file_type not in allowed_types:
            raise ValueError(
                f"type is: {file_type}, while it should be in {allowed_types}"
            )

        # root does not have parent
        self.name = name
        self.file_type = file_type
        self.size = size
        self.parent = parent
        self.children = []

        if self.parent:
            self.parent.add_child(self)

            # register size in parent object
            if self.file_type == "file":
                self.parent.add_size(self.size)

    def add_child(self, child):
        self.children.append(child)

    def add_size(self, size):
        # recurently add sum

        self.size += int(size)
        if self.parent:
            self.parent.add_size(size)

    def _print(self):
        print(
            f"parent: {(self.parent.name if self.parent else 'None')}, name: {self.name}, type: {self.file_type}, size: {self.size}, children: {self.children}"
        )


def cd(line, last_parent):
    if line.split()[2] == "..":
        return last_parent.parent

    dir_name = line.split()[2]
    for node in last_parent.children:
        if node.name == dir_name:
            return node


def build_tree(data):

    for line in data:

        # initiate tree
        if line == "$ cd /":
            root = Node(parent=None, name="/", file_type="dir")
            tree = [root]
            current_parent = root

        elif line[0:4] == "$ cd":
            current_parent = cd(line, current_parent)

        # handle ls
        elif line[0:4] == "$ ls":
            # not essential
            continue

        # handle dir
        elif line.split()[0] == "dir":
            name = line.split()[1]
            tree.append(Node(parent=current_parent, name=name, file_type="dir"))

        # handle file
        elif line.split()[0].isnumeric():
            size, name = line.split()[0], line.split()[1]
            tree.append(
                Node(parent=current_parent, name=name, size=size, file_type="file")
            )
        else:
            print("unexpected line, not ls/cd command, nor is it dir or file")

    return tree, root


def big_dirs(node, limit, lst=[]):
    # takes root of tree and dir size limit as arguments
    # lst - list will be appended with list of dirs that fit the requirements
    # returns list of directories above limit

    if int(node.size) >= limit:
        lst.append(int(node.size))

    children = [child for child in node.children if child.file_type == "dir"]
    # break if does not have children
    if children != []:
        for child in children:
            big_dirs(child, limit, lst)

    return lst


if __name__ == "__main__":

    file_data = read_file("day7.in")

    tree, root = build_tree(file_data)

    # calculate required space to free
    filesystem_ds = 70_000_000
    required_ds = 30_000_000
    space_to_save = required_ds - (filesystem_ds - root.size)

    # find smallest dir that fits the requirements
    dirs_list = big_dirs(root, space_to_save)
    dirs_list.sort()
    print(dirs_list[0])
