with open(0) as f:
  lines = f.readlines()

ans = 0
left = []
right = []

for line in lines:
    first, _, _, second = line.split(" ")
    left.append(int(first.strip()))
    right.append(int(second.strip()))

left.sort()
right.sort()

for index, num in enumerate(left):
    dist = right[index] - left[index]
    ans += abs(dist)

print(ans)
