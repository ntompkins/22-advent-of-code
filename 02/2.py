with open("input") as f:
    total,strat = 0,0
    outcomes = {
        "A":{"X":3,"Y":6,"Z":0},
        "B":{"X":0,"Y":3,"Z":6},
        "C":{"X":6,"Y":0,"Z":3}}
    score = {"X":1,"Y":2,"Z":3}
    strategy = {
        "A":{"X":score["Z"],"Y":3+score["X"],"Z":6+score["Y"]},
        "B":{"X":score["X"],"Y":3+score["Y"],"Z":6+score["Z"]},
        "C":{"X":score["Y"],"Y":3+score["Z"],"Z":6+score["X"]}}
    for line in f.readlines():
        line = line.strip().split()
        total += outcomes[line[0]][line[1]] + score[line[1]]
        strat += strategy[line[0]][line[1]]
    print(total, strat)

