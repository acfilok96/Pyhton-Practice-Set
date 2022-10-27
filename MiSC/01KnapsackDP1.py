def knapSack(W, weights, values):
   n = len(values)
   # Sort the weights in descending order
   p=[]
   for i,j in zip(weights,values):
      p.append([i,j])
   p=sorted(p, key = lambda x : x[0], reverse=False)
   weights = []
   values = []
   for i,j in p:
      weights.append(i)
      values.append(j)
   # Calculation
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   for i in range(n + 1):
      for w in range(W + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif weights[i-1] <= w:
            K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   return K[n][W]
#Main
values = [50,100,150,200]
weights = [8,16,32,40]
W = 64
print(knapSack(W, weights, values))
