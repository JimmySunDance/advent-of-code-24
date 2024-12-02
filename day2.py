# Day two of the Advent of Code 2024
# 
# Safe levels - Part 1
# Safe if all increasing or all decreasing
# Safe rate if 1 < x < 3
#

def safe(level):
    diff = [level[i] - level[i+1] for i in range(len(level)-1)]
    asc = all(map(lambda num: num in range(-3, 0), diff))
    dec = all(map(lambda num: num in range(1, 4), diff))
    return asc or dec

def main():

    with open("data/d2_safety_levels_r.txt", "r", encoding='utf-8') as f:
        levels = [line.rstrip('\n') for line in f]
    for i, l in enumerate(levels):
        levels[i] = [int(ll) for ll in l.split()]

    c1, c2 = 0,0
    for l in levels:
        if safe(l):
            c1 +=1
        if any(safe(l[:i] + l[i+1:]) for i in range(len(l))):
            c2 +=1
    
    print('Part 1 = ', c1)
    print('Part 2 = ', c2)
    
    return 
if __name__ == "__main__":
    main()