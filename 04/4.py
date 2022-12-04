with open("input") as f:
    counter,overlap = 0,0
    for line in f.read().splitlines():
        line = line.split(",")
        first, second = line[0].split("-"), line[1].split("-")
        r1 = [int(first[0]), int(first[1])]
        r2 = [int(second[0]), int(second[1])]
        if (r1[0] <= r2[0] and r1[1] >= r2[1]):
            counter += 1
        elif (r1[0] >= r2[0] and r1[1] <= r2[1]):
            counter += 1
        p1 = set(range(r1[0],r1[1]+1))
        p2 = set(range(r2[0],r2[1]+1))
        if (p1 & p2):
            overlap += 1
    print(counter, overlap)

