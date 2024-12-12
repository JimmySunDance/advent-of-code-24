# Day six of the Advent of Code 2024
# 
# Elf in a room
# 

def part_1(room, r, c):
    h, w = len(room), len(room[0])
    dr, dc = -1, 0

    seen = set()
    while True:
        seen.add((r, c))
        if r+dr < 0 or r+dr >= h or  c+dc < 0 or c+dc >= w: break
        if room[r + dr][c + dc] == '#':
            dr, dc = dc, -dr  # assigned at the same time
        else:
            r += dr
            c += dc

    return len(seen)


def will_it_loop(room, r, c):
    rows, cols = len(room), len(room[0])
    dr, dc = -1, 0
    seen = set()
    while True:
        seen.add((r, c, dr, dc))
        if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols: 
            return False
        if room[r + dr][c + dc] == '#':
            dr, dc = dc, -dr 
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True

def part_2(room, r, c):
    count = 0
    for cr in range(len(room)):
        for cc in range(len(room[0])):
            if room[cr][cc] != '.': continue
            room[cr][cc] = '#'
            if will_it_loop(room, r, c):
                count += 1
            room[cr][cc] = '.'

    return count



def main():
    room = open("data/d6_elf_patrol_r.txt", "r", encoding="utf-8").read()
    room = [list(l) for l in room.splitlines()]

    for r in range(len(room)):
        for c in range(len(room[0])):
            if room[r][c] == "^":
                break
        else:
            continue
        break

    p1 = part_1(room, r, c)
    print("Part 1: ", p1)

    p2 = part_2(room, r, c)
    print("Part 2: ", p2)

    return 

if __name__ == "__main__":
    main()