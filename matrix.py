# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter the elements row by row:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

# Display matrix
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
