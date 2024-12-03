def is_valid(level):
    n = len(level)
    inc = level[1] > level[0]
    for i in range(1, n):
        diff = level[i] - level[i - 1]
        if inc:
            if diff < 1 or diff > 3:
                return False
        else:
            if diff > -1 or diff < -3:
                return False
    return True

def is_valid_b(level):
    n = len(level)
    valid = False
    for i in range(n):
        a, b = 0, 1
        if i == 0: 
            a = 1
            b = 2
        elif i == 1:
            b = 2
        inc = level[b] > level[a]
        for j in range(1, n + 1):
            if j == n:
                valid = True
                break
            if j == i or (i == 0 and j == 1):
                continue
            prev = j - 1 if j - 1 != i else j - 2
            diff = level[j] - level[prev]
            if inc:
                if diff < 1 or diff > 3:
                    break
            else:
                if diff > -1 or diff < -3:
                    break

    return valid



def solve(i):
    totala = 0
    totalb = 0
    with open(i, 'r') as f:
        for line in f.readlines():
            if is_valid(list(map(int, line.split(" ")))):
                totala += 1
            if is_valid_b(list(map(int, line.split(" ")))):
                totalb += 1
    return totala, totalb


a, b = solve("input.txt")

print(f"Part 1: {a}")
print(f"Part 2: {b}")