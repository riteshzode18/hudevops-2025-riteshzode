def generate_pascals_triangle(n):
    # initialize a 2D list with zeros
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    # print(triangle)
    for i in range(n):
        for j in range(i + 1):

            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    
    return triangle

n = int(input("Enter the number of rows for Pascal's Triangle: "))

triangle = generate_pascals_triangle(n)

print("Output:")
for row in triangle:
    print(" ".join(map(str, row)))

