# Day two of the Advent of Code 2024
# 
# Safe levels - Part 1
# Safe if all increasing or all decreasing
# Safe rate if 1 < x < 3
#

def main():

    with open("data/d2_safety_levels_t.txt", "r", encoding='utf-8') as f:
        levels = [line.rstrip('\n') for line in f]

    for i, l in enumerate(levels):
        levels[i] = [int(ll) for ll in l.split()]
    
    print(levels)

if __name__ == "__main__":
    main()