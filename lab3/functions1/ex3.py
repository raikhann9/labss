#How many rabbits and how many chickens do we have?
def solve(numheads, numlegs):
    if numheads>numlegs:
        print("no solution")
    elif numlegs%2!=0:
        print("no solution")
    else:
        rabbits=(numlegs-numheads*2)/2
        chicken=numheads-rabbits
        print(int(rabbits), int(chicken))

numheads=35
numlegs=94
solve(numheads, numlegs)
