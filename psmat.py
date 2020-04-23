mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat[1][1] = 'x'  # update
print(mat)
print()

del mat[0][1]  # delete
print(mat)
print()

mat[2].append(10)  # append an item to the row
print(mat)
print()

mat[1].insert(2, 11)
print(mat)
print()

mat.insert(1, [22, 33, 44])  # insert a row
print(mat)
print()

for row in mat:
    for col in row:
        print(col, end='\t')
    print()


print(len(mat[0]))