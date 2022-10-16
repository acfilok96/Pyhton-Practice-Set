
def sum_func(n1,n2):
    n1,n2=str(n1),str(n2)
    n1=[i for i in n1]
    n2=[i for i in n2]
    if(len(n2)>len(n1)):
        pt=n1
        n1=n2
        n2=pt
    p=len(n1)-len(n2)
    n2=n2[::-1]
    for i in range(p):
        n2.append(str(0))
    n2=n2[::-1]
    # print(n1,n2)
    kk=[]
    temp=0
    for i,j in zip(n1[::-1],n2[::-1]):
        # print(i,j)
        pp=int(i)+int(j)+temp
        pp=[i for i in str(pp)]
        if(len(pp)==1):
            kk.append(pp[0])
            temp=0
        if(len(pp)>1):
            kk.append(pp[len(pp)-1])
            temp=int(pp[1])
    # print(int("".join(kk[::-1])))
    return int("".join(kk[::-1]))
    
# sum_func(101900000,2022)
n1=525711332872216331771389
n2=525711332872216331771387
n3=525711332872216331771387
n4=525711332872216331771387
n5=525711332872216331771387
n6=525711332872216331771387
n7=525711332872216331771387
n8=525711332872216331771385
n9=525711332872216331771387
n10=525711332872216331771387
####
nn1 = sum_func(n1,n2)
nn2 = sum_func(n3,n4)
nn3 = sum_func(n5,n6)
nn4 = sum_func(n7,n8)
nn5 = sum_func(n9,n10)
##
nnn1 = sum_func(nn1,nn2)
nnn2 = sum_func(nn3,nn4)
##
nnnn1 = sum_func(nnn1,nnn2)
## final
final = sum_func(nnnn1, nn5)
print(final)
