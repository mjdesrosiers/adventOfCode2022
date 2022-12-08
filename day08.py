import math


def score(path, me):
    taller = [you >= me for you in path]
    return (taller.index(True) + 1) if True in taller else len(taller)


if __name__ == "__main__":
    forest = []
    with open('input/day08_input.txt') as f:
        for line in f:
            forest.append([int(c) for c in line.strip()])
    forest_rot = list(zip(*forest))

    visible_trees = 0
    max_scenic_score = -1
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            me = forest[i][j]
            l = list(reversed(forest[i][:j]))
            r = forest[i][j + 1:]
            u = list(reversed(forest_rot[j][:i]))
            d = forest_rot[j][i + 1:]

            l_max = max(l or [-1])
            r_max = max(r or [-1])
            u_max = max(u or [-1])
            d_max = max(d or [-1])

            if any([me > tree for tree in [l_max, r_max, u_max, d_max]]):
                visible_trees += 1

            my_score = math.prod(score(path, me) for path in [l, r, u, d])
            max_scenic_score = max(max_scenic_score, my_score)

    print(f"Part 1: $visible_trees = {visible_trees}")
    print(f"Part 2: $maximum_scenic_score = {max_scenic_score}")
