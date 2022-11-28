import time
import numpy as np

def greedy(g,n):
    color=[-1]*n
    color[0]=1
    p=1
    l=[]
    for i in range(1,n):
        for j in range(0,i):
            if(g[i][j]==1):
                if(color[j]!=-1):
                    l.append(color[j])
        for j in range(1,p+1):
            if(j not in l):
                color[i]=j
                break
        if(color[i]==-1):
            p+=1
            color[i]=p
        l=[] 
    return color,p

def welsh_powell(g,n):
    deg={}
    k=0
    for i in range(n):
        for j in range(n):
            if(g[i][j]==1):
                k+=1
        deg[i]=k
        k=0
    sort_deg=sorted(deg.items(),key=lambda x:x[1],reverse=True)
    color=[-1]*n
    l1=[]
    f=0
    p=1
    l2=[]
    l=[i[0] for i in sort_deg] #getting sorted vertices
    for i in range(n):
        f=0
        if(l[i] in l2):
            continue
        color[l[i]]=p
        l2.append(l[i])
        for j in range(i+1,n):
            if(l[j] in l2):
                continue
            if(g[l[i]][l[j]]!=1):
                for x in l1:
                    if(g[x][l[j]]==1):
                        f=1
                if(f==1):
                    continue
                else:
                    color[l[j]]=p
                    l1.append(l[j])
                    l2.append(l[j])
        p+=1
        l1=[]
    return color,p-1

# Example 1:
# g=[[0,1,1,0,0],
#     [1,0,1,1,0],
#     [1,1,0,1,0],
#     [0,1,1,0,1],
#     [0,0,0,1,0]]
# n=5

# Example 2:
# g= [[0,1,1,1,0,0,1,0],
#     [1,0,0,0,1,1,0,0],
#     [1,0,0,0,0,0,1,0],
#     [1,0,0,0,0,0,1,0],
#     [0,1,0,0,0,1,0,1],
#     [0,1,0,0,1,0,0,1],
#     [1,0,1,1,0,0,0,1],
#     [0,0,0,0,1,1,1,0]]
# n=8

# for i in g:
#     print(i)


# Random undirected graphs generated using following code
n=27
g = np.random.randint(0,2,(n,n))
for i in range(n):
    for j in range(n):
        if(i==j):
            g[i][j]=0


print(g)


s1 = time.perf_counter()
c,p=greedy(g,n)
e1 = time.perf_counter()
ms1 = (e1-s1)* 10**6
print("\nGreedy Algo:")
print("Chromatic number : ",p,"\nIndices are vertices and values are colors of vertices : ",c)
print(f"{ms1:.03f} micro secs")

s2 = time.perf_counter()
c,p=welsh_powell(g,n)
e2 = time.perf_counter()
ms2 = (e2-s2)* 10**6
print("\nWelsh Powell Algo:")
print("Chromatic number : ",p,"\nIndices are vertices and values are colors of vertices : ",c)
print(f"{ms2:.03f} micro secs")

'''
Greedy Approach is fast, takes less time compared to Welsh Powell
since welsh powell must calculate degree of all vertices
and sort in descending order.

There are Two example cases where, in first example containing 5 vertices,
both algoithms give same chromatic number and distribution of colours,
Whereas in second example containing 8 vertices, greedy algo gave Chromatic
number as 3 while welsh powell gave chromatic number as 4.

Greedy approach depends on ordering of vertices, so if instead the order in 
2nd example was 0,6,2,3,1,5,4,7 then chromatic number would be 4. 
'''