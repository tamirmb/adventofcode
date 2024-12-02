with open(0) as f:
  lines = f.readlines()

ans = 0
left = []
right = {}

for line in lines:
    first, _, _, second = line.split(" ")
    first = first.strip()
    second = second.strip()

    left.append(int(first.strip()))

    if second in right:
        right[second] += 1
    else:
        right[second] = 1

for num in left:
    numstring = str(num)
    if numstring in right:
       ans += (num * right[numstring])

print(ans)
