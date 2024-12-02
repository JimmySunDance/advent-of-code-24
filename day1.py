# Day one of the Advent of Code 2024
# 
# Sort 2 lists - find the sum of the differences
# Multiply the value in list 1, byt the number of times it occurs in list 2
#

def similarity_difference_sum(list_a, list_b):
    list_a, list_b = sorted(list_a), sorted(list_b)
    s = []
    for i, _ in enumerate(list_a):
        s.append(abs(list_a[i] - list_b[i]))
    
    return sum(s)


def similarity_multi(list_a, list_b):
    total = []

    for i in list_a:
        j = 0
        for k in list_b:
            if i == k:
                j+=1
        
        total.append(i*j)
    return sum(total)


def main() -> None:
    with open("data/d1_location_list_r.txt", 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    a, b = [], []
    for l in lines:
        l = l.split()
        a.append(int(l[0]))
        b.append(int(l[1]))

    sum_score = similarity_difference_sum(a, b)
    multi_score = similarity_multi(a, b)
    print(sum_score, multi_score)
    return

if __name__ == "__main__":
    main()