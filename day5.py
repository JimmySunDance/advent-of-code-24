# Day five of the Advent of Code 2024
# 
import functools


def part_1(manual, update):
    count = 0
    for m in manual:
        good = True
        for up in update:
            if up[0] in m and up[1] in m:
                if m.index(up[0]) > m.index(up[1]): 
                    good = False
        if good:
            count += (m[(len(m) - 1)//2])

    return count


def is_ordered(m, rules):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            key = (m[i], m[j])
            if key in rules and rules[key] == 1:
                return False
    return True


def part_2(manual, update):
    count = 0

    rules = {}
    for up in update:
        rules[(up[0], up[1])] = -1
        rules[(up[1], up[0])] = 1

    def cmp(x, y): 
        return rules.get((x,y), 0)

    for m in manual: 
        if is_ordered(m, rules): continue
        m.sort(key=functools.cmp_to_key(cmp))
        count += (m[(len(m))//2])
    
    return count


def main():

    manual = open("data/d5_printing_error_r.txt", "r", encoding="utf-8").read()
    [update, manual] = manual.split('\n\n')

    manual = [list(map(int, man.split(','))) for man in manual.split('\n')]
    update = [list(map(int, up.split('|'))) for up in update.split('\n')]
    
    p1 = part_1(manual, update)
    p2 = part_2(manual, update)

    print("Part 1: ", p1)
    print("Part 2: ", p2)

    return 

if __name__ == "__main__":
    main()