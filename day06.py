if __name__ == "__main__":
    with open('input/day06_input.txt') as f:
        msg = f.readline()

    START_LEN = 4
    END_LEN = 14

    def find_unique_seq(count):
        gulps = [len(set(msg[n:n + count])) for n in range(len(msg) - count)]
        return gulps.index(count) + count

    print(find_unique_seq(START_LEN))
    print(find_unique_seq(END_LEN))
