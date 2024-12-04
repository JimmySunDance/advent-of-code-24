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

def part_2(input_string):
    on, total = True, 0
    for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", input_string):
        if match == "do()":
            on = True
        elif match == "don't()":
            on = False
        elif on:
            m = match[4:-1].split(',')
            total += int(m[0])*int(m[1])

    return total

def main():
    f = open("data/d3_corrupt_memory_r.txt", "r", encoding="utf-8").read()

    t1 = part_1(f)
    t2 = part_2(f)
    print('Part 1: ', t1)
    print('Part 2: ', t2)

    return 

if __name__ == "__main__":
    main()