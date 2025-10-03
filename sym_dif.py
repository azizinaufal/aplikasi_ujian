m = int(input())
data = map(int,input().split())
set1 = set(data)

n = int(input())
data2 = map(int,input().split())
set2 = set(data2)

dif = sorted(set1.symmetric_difference(set2))
for i in dif:
    print(i)

