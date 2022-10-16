
def func(str1, str2):
    p, q = len(str1), len(str2)

    arr = [[0 for i in range(q+1)] for j in range(p+1)]

    for i in range(1, p+1):
        for j in range(1, q+1):
            if (str1[i-1] == str2[j-1]):
                arr[i][j] = arr[i-1][j-1] + 1
            elif (str1[i-1] != str2[j-1]):
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    # for i in range(p+1):
    #     for j in range(q+1):
    #         print(arr[i][j], end='\t')
    #     print("\n")
    return arr[p][q]


str1 = 'agtcooooooo'
str2 = 'gctuooo'
print("\nLCS: ",func(str1, str2))
