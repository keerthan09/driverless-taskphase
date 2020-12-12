#1a

A = [[5,6,3],
    [7,3,8],
    [8,3,4]]
B = [[6,7,1,3],
    [7,2,9,4],
    [7,9,2,5]]
empty = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(A)):
            empty[i][j] += A[i][k] * B[k][j]
for r in empty:
    print(r)


#1b

X = [[5,6,7],
    [8,6,5],
    [4,3,3]]

empty = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(X))
    for j in range(len(X[0])):
        empty[j][i] = X[i][j]

for r in empty
    print (r)

#2a


t=(2,6,4,9,1,8,6,9,2)
l=[]
for i in t:
    if i in l:
        continue
    else:
        l.append(i)
l=tuple(l)
print(l)

#2b

dep sum_l(l,side):
    if (size == 0):
        return 0
    else:
        return l[size-1] + sum_l(l,size-1)
b=sum_l(l,len(l))
print("sum of items in list:",b)
