import copy

if __name__ == "__main__":
    columns = []

    with open('input/day05_input.txt') as f:
        # get stack data
        stacklines = []
        while True:
            line = f.readline().rstrip()
            if not len(line):
                break
            stacklines.append(line)
        column_names = stacklines.pop().strip().split()
        cols_to_keep = [(4 * i + 1) for i in range(len(column_names))]

        for line in stacklines:
            if len(line) > len(columns):
                columns.extend([[] for n in range(len(line) - len(columns))])
            for i, ch in enumerate(line):
                columns[i].append(ch)

        data_columns = [columns[i] for i in cols_to_keep]
        data_columns = [[item for item in col if (len(item.strip()))]
                        for col in data_columns
                        ]

        columns_s1 = copy.deepcopy(data_columns)
        columns_s2 = copy.deepcopy(data_columns)

        while True:
            line = f.readline().strip().split()
            if not line:
                break
            n = int(line[1])
            col_from = int(line[3]) - 1
            col_to = int(line[5]) - 1

            # strategy 1
            for i in range(n):
                columns_s1[col_to].insert(0, (columns_s1[col_from].pop(0)))

            # strategy 2
            moved = columns_s2[col_from][0:n]
            del columns_s2[col_from][0:n]
            columns_s2[col_to] = moved + columns_s2[col_to]

    output_1 = "".join(col[0] for col in columns_s1)
    print(output_1)
    output_2 = "".join(col[0] for col in columns_s2)
    print(output_2)
