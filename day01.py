if __name__ == "__main__":
    calorie_totals = []
    filename = 'input/day01_input.txt'

    lines = None
    with open(filename) as f:
        lines = f.readlines()

    complete_text = "".join(lines)
    elf_texts = complete_text.split("\n\n")
    elf_texts = [elf_text.strip().split('\n') for elf_text in elf_texts]
    elf_calories = []
    for elf_text in elf_texts:
        elf_calories.append(sum([int(_) for _ in elf_text]))
        print(elf_calories[-1])

    max_cals = max(elf_calories)
    max_idx = elf_calories.index(max_cals)
    print(f"Part 1: max calories on an elf = {max_cals}")

    calories_sorted = list(reversed(sorted(elf_calories)))
    top_3_calories = sum(calories_sorted[0:3])
    print(f"Part 2: top three elves' calories = {top_3_calories}")
