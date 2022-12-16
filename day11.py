import copy
from operator import mul, add

str_to_fcn = {
    "*": mul,
    "+": add
}


class Monkey:
    def __init__(self, lines):
        self.idx = int(lines[0].split()[1][:-1])
        self.items = [int(part) for part in lines[1].split(":")[1].strip().split(", ")]
        op_parts = lines[2].split()
        self.operator = str_to_fcn[op_parts[4]]
        try:
            self.operand = int(op_parts[5])
        except:
            self.operand = None
        self.div_by = int(lines[3].split("by ")[1])
        self.monkey_true = int(lines[4].split("monkey ")[1])
        self.monkey_false = int(lines[5].split("monkey ")[1])
        self.n_inspections = 0

    def inspect(self, old):
        self.n_inspections += 1
        if self.operand:
            return self.operator(old, self.operand)
        else:
            return self.operator(old, old)

    def test(self, val):
        return (val % self.div_by) == 0

    def __str__(self):
        return (f"Monkey # = {self.idx} with vals = {self.item} and expr = {self.op_expr}\n"
                f"divby = {self.div_by}, T={self.monkey_true}, F={self.monkey_false}")


def product(values):
    tot = 1
    for v in values:
        tot *= v
    return tot


def do_monkey_rounds(monkeys, count, relax=None):
    rlx = lambda x: x // relax
    if not relax:
        relax = product([monkey.div_by for monkey in monkeys])
        rlx = lambda x: x % relax
    for i in range(count):
        monkeys = do_round(monkeys, rlx)

    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i} inspected items {monkey.n_inspections} times")

    inspection_counts = sorted([m.n_inspections for m in monkeys], reverse=True)
    monkey_business = inspection_counts[0] * inspection_counts[1]
    return monkey_business


def do_round(monkeys, relaxation):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            _worry_level = monkey.inspect(item)
            worry_level = relaxation(_worry_level)
            if monkey.test(worry_level):
                monkeys[monkey.monkey_true].items.append(worry_level)
            else:
                monkeys[monkey.monkey_false].items.append(worry_level)
            monkey.items = []
    return monkeys


if __name__ == "__main__":
    monkeys = []
    with open('input/day11_input.txt') as f:
        line = f.readline()
        while line:
            line = line.strip()
            parts = line.split()
            if parts and parts[0] == "Monkey":
                monkey_lines = [f.readline().strip() for i in range(5)]
                monkey_lines.insert(0, line)
                monkeys.append(Monkey(monkey_lines))
            line = f.readline()

    monkey_business = do_monkey_rounds(copy.deepcopy(monkeys), 20, 3)
    print(f"$pt1: monkey business = {monkey_business}")

    monkey_business = do_monkey_rounds(copy.deepcopy(monkeys), 10_000)
    print(f"$pt2: monkey business = {monkey_business}")
