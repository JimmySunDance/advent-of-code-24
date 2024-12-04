# Day three of the Advent of Code 2024
# 
# Extract valid "mul(X,Y)" statements, multiply the values and sum the results
#
#
import re

def part_1(input_string):
    total = 0
    for match in re.findall(r'mul\(\d{1,3},\d{1,3}\)', input_string):
        m = match[4:-1].split(',')
        total += int(m[0])*int(m[1])
    return total 

def main():
    f = open("data/d3_corrupt_memory_r.txt", "r", encoding="utf-8").read()

    total = part_1(f)
    print('Part 1: ', total)

    return 

if __name__ == "__main__":
    main()