# Day two of the Advent of Code 2024
# 
# Safe levels - Part 1
# Safe if all increasing or all decreasing
# Safe rate if 1 < x < 3
#

def part_1(levels_array):
    x = []
    for line in levels_array:
        l = True

        if line[-1] == line[0]:
            l = False

        if line[-1] > line[0]:
            for i in range(len(line)-1):
                diff = line[i] - line[i+1]
                if diff < -3 or diff > -1:
                    l = False
                    break
        
        if line[-1] < line[0]:
            for i in range(len(line)-1):
                diff = line[i] - line[i+1]
                if diff not in range(1, 3): #diff > 3 or diff < 1:
                    l = False
                    break
        x.append(l)
    
    return sum(x)

def part_2(levels_array):
    x = []
    for line in levels_array:
        print(line)
        l = False
        if line[-1] == line[0]:
            l = False
        
        damper = 0
        print('d - ', damper)
        if line[-1] > line[0]:
            for i in range(len(line)-1):
                diff = line[i] - line[i+1]
                print(diff)
                if diff < -3 or diff > -1:
                    damper += 1
        
        if line[-1] < line[0]:
            for i in range(len(line)-1):
                diff = line[i] - line[i+1]
                print(diff)
                if diff > 3 and diff < 1:
                    damper += 1                    
    
        if damper > 2:
            l = True
        print(damper, l)
        
        x.append(l)

    return sum(x)

def main():

    with open("data/d2_safety_levels_r.txt", "r", encoding='utf-8') as f:
        levels = [line.rstrip('\n') for line in f]
    for i, l in enumerate(levels):
        levels[i] = [int(ll) for ll in l.split()]

    p1 = part_1(levels)
    p2 = part_2(levels)
    print(p1, p2)
    
    return 

if __name__ == "__main__":
    main()