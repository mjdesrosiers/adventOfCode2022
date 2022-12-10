directions = {
    "U": (-1, 0),
    "D": (+1, 0),
    "L": (0, -1),
    "R": (0, +1)
}


def add_vec(a, b):
    return tuple(sum(pair) for pair in zip(a, b))


def sub_vec(a, b):
    return tuple(v[0] - v[1] for v in zip(a, b))


def limit_vec_posneg_to(a, lim):
    pos_limit = tuple(min(v, lim) for v in a)
    neg_limit = tuple(max(v, -1 * lim) for v in pos_limit)
    return neg_limit


def print_board(s):  # likely to crash if called
    board = [["." for __ in range(15)] for _ in range(15)]
    for i in reversed(range(len(segments))):
        board[s[i][0]][s[i][1]] = str(i)
    lines = ["".join(lin) for lin in board]
    print("\n".join(lines) + '\n')


if __name__ == "__main__":
    moves = []
    with open('input/day09_input.txt') as f:
        for line in f:
            way, num = line.strip().split()
            moves.append((directions[way], int(num)))

    n_segments = 10

    segments = [(0, 0) for _ in range(n_segments)]
    segment_positions = [set() for _ in range(n_segments)]

    # Loop level 0: go through each direction/count pair
    for mod, cnt in moves:
        # Loop level 1: go through each repetition of the move
        for i in range(cnt):
            # Loop level 2: see how it effects each segment
            for j in range(len(segments)):
                if j == 0:  # special case for head
                    segments[j] = add_vec(segments[0], mod)
                else:       # case for every other segment
                    # Segments only move if they're off by > 2 in any direction
                    diff = sub_vec(segments[j-1], segments[j])
                    if any(abs(d) > 1 for d in diff):
                        my_move = limit_vec_posneg_to(diff, 1)
                        segments[j] = add_vec(segments[j], my_move)
                segment_positions[j].add(segments[j])
            # make_board(segments)

    print(f"$pt1_positions_visited => {len(segment_positions[+1])}")
    print(f"$pt2_positions_visited => {len(segment_positions[-1])}")
