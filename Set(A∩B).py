size_a=int(input())
a=set(list(map(int, input().strip().split()))[:size_a])
size_b=int(input())
b=set(list(map(int, input().strip().split()))[:size_b])
print(len(a^b))
