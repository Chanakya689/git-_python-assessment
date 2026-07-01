#Given Input: Rows: 5 
# Expected Output: 
# [1] 
# [1, 1] 
# [1, 2, 1] 
# [1, 3, 3, 1] 
# [1, 4, 6, 4, 1]

def generate_pascals_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

rows = 5
triangle = generate_pascals_triangle(rows)
for row in triangle:
    print(row)