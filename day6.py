# Day six of the Advent of Code 2024
# 

def part_1(room, pos, facing):
    h, w = len(room), len(room[0])

    travelled = [pos]
    while pos[0] in range(0, h-1) and pos[1] in range(0, w-1):
        if facing == "^":
            n_pos = (pos[0]-1, pos[1])
            if room[n_pos[0]][n_pos[1]] == "#":
                facing = ">"
            else: 
                pos = n_pos
                if pos[0] in range(0, h-1) and pos[1] in range(0, w-1):
                    travelled.append(pos)
            
        if facing == ">":
            n_pos = (pos[0], pos[1]+1)
            if room[n_pos[0]][n_pos[1]] == "#":
                facing = "v"
            else: 
                pos = n_pos
                if pos[0] in range(0, h-1) and pos[1] in range(0, w-1):
                    travelled.append(pos)
            
        if facing == "v":
            n_pos = (pos[0]+1, pos[1])
            if room[n_pos[0]][n_pos[1]] == "#":
                facing = "<"
            else: 
                pos = n_pos
                if pos[0] in range(0, h-1) and pos[1] in range(0, w-1):
                    travelled.append(pos)
            
        if facing == "<":
            n_pos = (pos[0], pos[1]-1)
            if room[n_pos[0]][n_pos[1]] == "#":
                facing = "^"
            else: 
                pos = n_pos
                if pos[0] in range(0, h-1) and pos[1] in range(0, w-1):
                    travelled.append(pos)

    return len(set(travelled))

def main():
    room = open("data/d6_elf_patrol_r.txt", "r", encoding="utf-8").read()
    room = [l for l in room.splitlines()]

    for r in range(len(room)):
        for c in range(len(room[0])):
            if room[r][c] in "^>v<":
                facing = room[r][c]
                pos = (r, c)

    p1 = part_1(room, pos, facing)

    print("Part 1: ", p1)

    return 

if __name__ == "__main__":
    main()