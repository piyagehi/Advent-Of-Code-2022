t1, t2 = 'ABC','XYZ'
p1, p2 = 0,0
rounds = [i.split() for i in open('input').read().splitlines()]

for r in rounds:
    result = t2.find(r[1]) - t1.find(r[0])
    p1 += (6 if result == 1 or result == -2 else 3 if not result else 0) + t2.find(r[1]) + 1
    p2 += (6 + (t1.find(r[0]) + 1) % 3 if r[1] == 'Z' else 3 + t1.find(r[0]) if r[1] == 'Y' else (t1.find(r[0]) - 1) % 3) + 1

print("Part One:", p1, "Part Two:", p2)
