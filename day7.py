# Day seven of the Advent of Code 2024
# 
# Rope bridge and elephants
# 

def can_obtain(t, v):
    if len(v) == 1: return t == v[0]
    if t % v[-1] == 0 and can_obtain(t // v[-1], v[:-1]): return True
    if t > v[-1] and can_obtain(t - v[-1], v[:-1]): return True
    return False


def part_1(targets, values):
    total = 0
    for t, v in zip(targets, values):
        if can_obtain(t, v):
            total += t
    
    return total

def main():

    inst = open('data/d7_elephants_r.txt', 'r', encoding='utf-8').read()
    targets, vals = [], []
    for line in inst.splitlines():
        [t, v] = line.split(':')
        targets.append(int(t))
        vals.append([int(i) for i in v.split()])
    
    p1 = part_1(targets, vals)
    print("Part 1: ", p1)

    return 

if __name__ == "__main__":
    main()