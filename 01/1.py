with open('input') as f:
    elves = [0]
    for line in f.readlines():
        if (line.strip()):
            elves[-1] += int(line)
        else:
            elves.append(0)
    elves.sort(reverse=True)
    print(elves[0], elves[0]+elves[1]+elves[2])
