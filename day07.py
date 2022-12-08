
def add_file_to_listing(directory, structure, arg1, arg2, depth):
    if depth >= len(directory):  # if we're all the way down
        try:
            structure[arg2] = int(arg1)
        except:
            pass
        return structure
    else:   # delve deeper
        go_to_dir = directory[depth]
        if go_to_dir not in structure:
            structure[go_to_dir] = {}
        structure[go_to_dir] = add_file_to_listing(directory, structure[go_to_dir],
                                                   arg1, arg2, depth + 1)
        return structure


def find_directory_size(structure):
    if type(structure) == int:
        return structure
    else:
        size = 0
        for filename in structure:
            size += find_directory_size(structure[filename])
        return size


"""
    Do some shady stuff with directory naming -- need to make sure that duplicate
    directory names do not shadow each other, so when we do tallies, do it with 
    an absolute-style path
"""
def find_directory_sizes(structure, name='/', prefix=""):
    sizes = {}
    if prefix:
        fullname = prefix + "-" + name
    else:
        fullname = name
    sizes[fullname] = find_directory_size(structure)
    for filename in structure:
        if type(structure[filename]) is not int:
            sizes = sizes | find_directory_sizes(structure[filename], filename, fullname)
    return sizes


def print_structure(structure, indent=1):
    size = 0
    if indent == 1:
        print(f"- / (dir) => {find_directory_size(structure)}")
    for file in structure:
        if type(structure[file]) == int:
            pass # print("\t" * indent + f"{file} (file) => {structure[file]}")
        else:
            size = find_directory_size(structure[file])
            print("\t" * indent + f"- {file} (dir) => {size}")
            print_structure(structure[file], indent + 1)


if __name__ == "__main__":
    structure = {}
    current_dir = []

    with open('input/day07_input.txt') as f:
        for line in f:
            line = line.strip()
            parts = line.split("$ ")
            if len(parts) > 1:
                command_parts = parts[1].split()
                if command_parts[0] == "cd":
                    if command_parts[1] == "..":
                        current_dir = current_dir[:-1]
                    else:
                        current_dir.append(command_parts[1])
            else:
                arg1, arg2 = parts[0].split()
                structure = add_file_to_listing(current_dir[1:], structure, arg1, arg2, 0)

    # print_structure(structure)
    directory_sizes = find_directory_sizes(structure)

    PT_1_THRESH = 100000
    threshold_sizes = [directory_sizes[k] for k in directory_sizes
                       if directory_sizes[k] <= PT_1_THRESH]
    deleteable_size = sum(threshold_sizes)
    print(f"PART 1: ==> $deleteable_size = {deleteable_size}")

    TOTAL_DISK_SPACE = 70000000
    NEEDED_SPACE     = 30000000

    used_space = directory_sizes['/']
    free_space = TOTAL_DISK_SPACE - used_space
    additional_to_delete = NEEDED_SPACE - free_space

    directory_sizes = [directory_sizes[k] for k in directory_sizes
                       if directory_sizes[k] > additional_to_delete]
    smallest_deleteable_directory_size = min(directory_sizes)
    print(f"PART 2: ==> $smallest_deleteable_directory_size = {smallest_deleteable_directory_size}")
