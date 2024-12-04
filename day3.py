# Day three of the Advent of Code 2024
# 
# Extract valid "mul(X,Y)" statements, multiply the values and sum the results
#
#
import re

def main():
    f = open("data/d3_corrupt_memory_r.txt", "r", encoding="utf-8").read()
    mul_split = f.split('mul(')
    filter1 = [c for c in mul_split if c[0].isnumeric()]
    
    a = []
    for f in filter1:
        f = f.split(')')
        a.append(f[0])
    a = [i for i in a if i[-1].isnumeric()]
    
    b = []
    for i in a:
        i = i.split(',')
        b.append(int(i[0]) * int(i[1]))

    print('Part 1: ', sum(b))
    return 

if __name__ == "__main__":
    main()