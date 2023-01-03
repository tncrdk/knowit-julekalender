
def Formatting(link):
    with open(link) as f:
        txt = f.read().split()
    
    txt = [[x for x in i] for i in txt]
    length = len(txt[0])
    txt.insert(0, ["0"]*length)
    txt.append(["0"]*length)
    for i in txt:
        i.insert(0, "0")
        i.append("0")

    return txt


def GoingToGetSick(Map):
    Infected = []
    for y in range(1, len(Map)-1):
        for x in range(1, len(Map[0])-1):
            NumSick = 0
            if Map[y][x] == "F":
                if Map[y+1][x] == "S":
                    NumSick += 1
                if Map[y-1][x] == "S":
                    NumSick += 1
                if Map[y][x+1] == "S":
                    NumSick += 1
                if Map[y][x-1] == "S":
                    NumSick += 1
            
                if NumSick >= 2:
                    Infected.append((y, x))
    
    return Infected


def UpdateMap(Map, Infected):
    for i in Infected:
        Map[i[0]][i[1]] = "S"
    
    return Map


def Repeated(Map):
    counter = 0
    Infected = [1]
    while len(Infected) != 0:
        Infected = GoingToGetSick(Map)
        Map = UpdateMap(Map, Infected)
        counter += 1
    
    print(counter)


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Knowit-Julekalender\\09-des\\Sick_People.txt"

Map = Formatting(link)

Repeated(Map)
