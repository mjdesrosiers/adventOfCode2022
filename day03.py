
def character_to_value(character):
    value = None
    if ord(shared) > ord('a'):
        value = ord(shared) - ord('a') + 1
    else:
        value = ord(shared) - ord('A') + 26 + 1
    return value

if __name__ == "__main__":
    score = 0

    # part 1
    with open('input/day03_input.txt') as f:
        for line in f:
            line = line.strip()
            mid = int(len(line)/2)
            compartment_1 = set(line[0:mid])
            compartment_2 = set(line[mid:])
            shared = list(compartment_2.intersection(compartment_1))[0]
            value = character_to_value(shared)
            score = score + value
        print(f"Part 1 score: {score}")


    # part 2
    with open('input/day03_input.txt') as f:
        trio_strings = []
        score = 0
        while True:
            line = f.readline()
            if not line:
                break
            trio_strings.append(set(line.strip()))
            if len(trio_strings) == 3:
                unique = trio_strings[0].intersection(trio_strings[1]).intersection(trio_strings[2])
                shared = list(unique)[0]
                value = character_to_value(shared)
                score = score + value
                trio_strings = []
        print(f"Part 2 score: {score}")



