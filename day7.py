# Day seven of the Advent of Code 2024
# 
# Rope bridge and elephants
# 

def part_1():
    return 

def main():

    inst = open('data/d7_elephants_t.txt', 'r', encoding='utf-8').read()
    target, vals = [], []
    for line in inst.splitlines():
        [t, v] = line.split(':')
        target.append(int(t))
        vals.append(list(map(int, [i for i in v.split()])))
    
    print(target)
    print(vals)

    return 

if __name__ == "__main__":
    main()