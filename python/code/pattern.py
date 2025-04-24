# first pattern

rows = 5

for i in range(1, rows + 1):

    for space in range(1, rows - i + 1):
        print(" ", end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()  


print()
# 2nd pattern
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i, rows):
        print("*", end=" ")
    print()