

if __name__ == "__main__":
    score = 0

    # part 1
    with open('input/day04_input.txt') as f:
        count_pt1 = 0
        count_pt2 = 0
        for line in f:
            line = line.strip()
            n1, n2, n3, n4 = [int(n) for n in line.replace(',', '-').split('-')]
            first_nums = set(range(n1, n2 + 1))
            second_nums = set(range(n3, n4 + 1))
            if first_nums.issubset(second_nums) or second_nums.issubset(first_nums):
                count_pt1 = count_pt1 + 1
            if len(first_nums.intersection(second_nums)):
                count_pt2 = count_pt2 + 1


        print(f"Part 1 count: {count_pt1}")
        print(f"Part 2 count: {count_pt2}")


