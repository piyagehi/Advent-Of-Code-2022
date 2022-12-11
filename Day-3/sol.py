priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
p1, p2 = 0, 0
lst = open('input').read().splitlines()
for l in range(len(lst)):
    p1 += priority.find(''.join(set(lst[l][:len(lst[l])//2]) & set(lst[l][len(lst[l])//2:]))) + 1
    if l % 3 == 0:
        p2 += priority.find(''.join(set(lst[l]) & set(lst[l+1]) & set(lst[l+2]))) + 1
print("Part One:", p1, "Part Two:", p2)