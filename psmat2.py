mat = [[1],
       [4, 5, 6],
       [7, 9]]


for row in mat:
    while True:
        if len(row) == 3:
            break
        row.append(0)

print(mat)