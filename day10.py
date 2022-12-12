class AddOp:
    def __init__(self, initial_count, arg):
        self.arg = int(arg[0])
        self.expiry = initial_count + 2


class NoopOp:
    def __init__(self, initial_count, *args):
        self.arg = 0
        self.expiry = initial_count + 1

op_types = {
    "addx": AddOp,
    "noop": NoopOp
}

class OpExpiry:
    def __init__(self, when, arg):
        self.when = when
        self.arg = arg

    def expired(self, count):
        return count == self.when


def stringify_number(num, pad_to=40):
    base = f"{num:#040b}"[2:][::-1].replace("0", '.').replace("1", "#")
    base = base + "." * (pad_to - len(base))
    return base


class Program:
    def __init__(self):
        self.pgm_ctr = 0
        self.total = 1
        self.op_current = None
        self.ops_waiting_on = []
        self.strengths = {}
        self.drawn_lines = [0, 0, 0, 0, 0, 0, 0]

    def add_op(self, opcode, rest):
        self.op_current = op_types[opcode](self.pgm_ctr, rest)
        self.ops_waiting_on.append(
            OpExpiry(self.op_current.expiry, self.op_current.arg)
        )

    def finish_op(self):
        while self.pgm_ctr < self.op_current.expiry:
            self.pgm_ctr += 1

            if (self.total - 1) < 0:                        # Pt2: find sprite position
                sprite_mask = 0
            else:
                sprite_mask = 0b111 << (self.total-1)
            drawable_mask = 1 << ((self.pgm_ctr-1) % 40)    # Pt2: find where we're drawing now
            drawn = sprite_mask & drawable_mask             # Pt2: Find new drawn character
            self.drawn_lines[self.pgm_ctr // 40] |= drawn   # Pt2: add to drawn

            # Pt1: update strengths based on total
            self.strengths[self.pgm_ctr] = (self.pgm_ctr * self.total)
            # Find new total
            self.total += sum(
                op.arg for op in self.ops_waiting_on if op.expired(self.pgm_ctr)
            )

    def signal_at_cycle(self, idx):
        return self.strengths[idx]

    def show_crt(self):
        for line in self.drawn_lines:
            print(stringify_number(line))
        print()


if __name__ == "__main__":
    with open('input/day10_input.txt') as f:
        lines = [line.strip().split() for line in f.readlines()]

    Prog = Program()
    for line in lines:
        Prog.add_op(line[0], line[1:])
        Prog.finish_op()

    Prog.show_crt()

    inspects = [20, 60, 100, 140, 180, 220]
    pt1_answer = sum(Prog.signal_at_cycle(inspect) for inspect in inspects)
    print(f"$pt1 => {pt1_answer}")
