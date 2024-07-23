#!/usr/bin/python3.8

rows = [[1]]

display_type = "row"

inp = input("> ").strip().split(' ')

if len(inp) == 2:
    n, display_type = inp
    n = int(n)
else:
    n = int(inp[0])

for r in range(1, n + 1):
    row = []
    for i, _ in enumerate(rows[r-1]):
        if i == 0:
            row.append(1)
        else:
            row.append(rows[r-1][i - 1] + rows[r-1][i])
    row.append(1)
    rows.append(row)

if display_type == "tri":
    for r in rows:
        print(' '.join([str(i) for i in r]))
elif display_type == "row":
    print(' '.join([str(i) for i in rows[n]]))
else:
    print(f"Invalid display type '{display_type}'")
