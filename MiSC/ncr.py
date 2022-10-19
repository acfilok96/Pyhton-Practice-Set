def ncr(n,r):
    mat=[[0 for i in range(r)] for j in range(n)]
    
    for i in range(n):
        for j in range(r):
            if(j==0):
                mat[i][j]=i+1
            elif(i<j):
                mat[i][j]=0
            elif(i==j):
                mat[i][j]=1
            else:
                mat[i][j]=mat[i-1][j-1]+mat[i-1][j]
    return mat[n-1][r-1]

print(ncr(40,3)) 