entries = [i.splitlines() for i in open('input').read().split("\n\n")]
for i in range(len(entries)):
    entries[i] = sum([int(x) for x in entries[i]])
print("Part One:", max(entries), "Part Two:", sum(sorted(entries, reverse=True)[:3]))