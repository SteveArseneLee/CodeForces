# Input
# The input consists of five lines, each line contains five integers: 
# the j-th integer in the i-th line of the input represents the element of the matrix that 
# is located on the intersection of the i-th row and the j-th column. It is guaranteed that the 
# matrix consists of 24 zeroes and a single number one.

# Output
# Print a single integer — the minimum number of moves needed to make the matrix beautiful.

# 아름답게 움직인다는 것은 (3,3)인 한가운데 있어야하는것임.
lst = [list(map(int,input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if lst[i][j] == 1:
            print(abs(i-2) + abs(j-2))
            break