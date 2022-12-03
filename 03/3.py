with open("input") as f:
    total,groups = 0,0
    while True:
        elves = [f.readline().strip(), f.readline().strip(), f.readline().strip()]
        if not elves[0]: break
        for sack in elves:
            common = list(set(sack[:len(sack)//2]) & set(sack[len(sack)//2:]))[0]
            total += ord(common) - (38 if common.isupper() else 96)
        badge = list(set(elves[0]).intersection(set(elves[1]), set(elves[2])))[0]
        groups += ord(badge) - (38 if badge.isupper() else 96)
    print(total,groups)

