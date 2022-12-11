p1, p2 = 0, 0
entries = [[set(range(int(i.split(',')[k].split('-')[0]), int(i.split(',')[k].split('-')[1])+1)) for k in range(2)] for i in open('input').read().splitlines()]
p1 = sum([1 for i in entries if i[0].issubset(i[1]) or i[1].issubset(i[0])])
p2 = sum([1 for i in entries if i[0].intersection(i[1])])
print("Part One:", p1, "Part Two:", p2)