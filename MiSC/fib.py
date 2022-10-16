def fib_itr(n):
    n1,n2=0,1
    print(n1,'\t',n2,'\t')
    val=0
    for i in range(2,n):
        val=n1+n2
        print(val,end='\t')
        n1=n2
        n2=val
    return val
def fib_rec(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fib_rec(n-1)+fib_rec(n-2)
def fib_memo(n):
    arr = [i for i in range(n)]
    arr[0],arr[1]=0,1
    print(0,arr[0])
    print(1,arr[1])
    for i in range(2,n):
        arr[i] = arr[i-1]+arr[i-2]
        print(i,arr[i])
    return arr[n-1]
# fib_itr(9)
# print(fib_rec(9))
# print(fib_memo(9))