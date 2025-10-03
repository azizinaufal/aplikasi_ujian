# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
value = set(map(int, input().split()))
N = int(input())

for i in range(N):
    parts = input().split()
    command = parts[0]
    if command == "discard":
        x = int(parts[1])
        if x in value:
            value.discard(x)
    elif command == "remove":
        x = int(parts[1])
        if x in value:
            value.remove(x)
    elif command == "pop":
        if value:
            value.pop()

print(sum(value))
