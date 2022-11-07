# Integer Partition Problem
# p(5) = 7
# p(50) = 204226
# p(100) = 190569292

# More Details: https://en.wikipedia.org/wiki/Partition_function_(number_theory)

def IntegerPartitionProblem(n):
    mat=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        mat[i][0]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i>j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-i]
    return mat[n][n]

n=100
result = IntegerPartitionProblem(n)
print("Result: ", result)