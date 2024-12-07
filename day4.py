# Day four of the Advent of Code 2024
# 
# Find how many time the string "XMAS" exists in the grid. It can exist in all 
# orientations.
# Find instances of an X mad of the word MAS
# M - M
# - A -
# S - S
#

def part_1(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "X": continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0: continue

                    in_row = 0 <= r + 3 * dr < len(grid)
                    in_col = 0 <= c + 3 * dc < len(grid[0])
                    if not (in_row and in_col): continue
                    
                    g_M = grid[r + dr][c + dc] == "M"
                    g_A = grid[r + 2 * dr][c + 2 * dc] == "A"
                    g_S = grid[r + 3 * dr][c + 3 * dc] == "S"
                    if g_M and g_A and g_S:
                        count +=1
    return count 

def part_2(grid):
    count = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] != "A": continue
            corners = [
                grid[r-1][c-1], grid[r-1][c+1],
                grid[r+1][c+1], grid[r+1][c-1]
            ]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                count += 1
                                
    return count

def main():

    grid = open("data/d4_xmas_search_r.txt", "r", encoding="utf-8").read()
    grid = grid.splitlines()

    p1 = part_1(grid)
    p2 = part_2(grid)

    print('Part 1: ', p1)
    print('Part 2: ', p2)

    return 

if __name__ == "__main__":
    main()