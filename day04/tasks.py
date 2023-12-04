import numpy as np
lines = []
res = 0
with open("input.txt", "r") as f:
    for line in f:
        lines.append([l.strip() for l in line.split('|')])
points = np.zeros(len(lines), dtype=int)
for ind, line in enumerate(lines):
    inn = np.array([int(a) for a in line[0].split(':')[1].strip().split(" ") if a != ''])
    outt = np.array([int(a) for a in line[1].split(" ") if a != ''])
    mapp = np.zeros(1000, dtype=int)
    mapp[inn] = 1
    ress = np.sum(mapp[outt])
    points[ind] = ress
    if ress > 0:
        res += 2**(ress - 1)
print(f"Part 1: {res}")

cards_count = np.ones_like(points, dtype=np.int64)

for ind in range(len(points)):
    try:
        for i in range(points[ind]):
            cards_count[ind+1+i] += cards_count[ind]
    except Exception as e:
        pass
print(f"Part 2: {np.sum(cards_count)}")
