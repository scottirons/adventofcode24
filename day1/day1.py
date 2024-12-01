from collections import Counter

def solve(source):
    first = []
    second = []
    with open(source, 'r') as f:
        for line in f.readlines():
            a, b = line.split()
            first.append(int(a))
            second.append(int(b))
    
    first.sort()
    second.sort()

    pt2 = Counter(second)

    totala = sum(abs(second[i] - first[i]) for i in range(len(first)))
    totalb = sum(i * pt2[i] for i in first)
    print(f"Part A: {totala}")
    print(f"Part B: {totalb}")

solve("input.txt")