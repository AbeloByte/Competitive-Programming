m,n = map(int,(input().strip().split()))
list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))
i = 0
result = []
for j in range(n):
    while i < m and list1[i] < list2[j]:
        i+=1
    result.append(i)
 
print(*result)
