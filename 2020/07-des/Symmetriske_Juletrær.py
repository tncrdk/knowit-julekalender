
def Formatting(link):    
    with open(link) as f:
        forest = f.readlines()

    return forest


def Checking_for_Symmetri(forest, rot_index):
    y = -2
    Symmetrisk = True
    while abs(y) < len(forest):
        To_på_rad = 0
        høyre = venstre = rot_index
        while To_på_rad < 2:
            høyre += 1
            venstre -= 1
            if forest[y][høyre] != forest[y][venstre]:
                Symmetrisk = False
                return Symmetrisk
            if forest[y][venstre] == " ":
                To_på_rad += 1
        
        y -= 1
    
    return True


def Checking_Every_Tree(forest, Stamme_Index):
    counter = 0
    for i in Stamme_Index:
        if Checking_for_Symmetri(forest, i):
            counter += 1
    
    print(counter)


# =============================================================================
# Functions
# Execution
# =============================================================================


link = "C:\\Users\\thorb\\Documents\\Python\\Knowit-Julekalender\\07-des\\Juletrær.txt"

forest = Formatting(link)

Stamme_Index = []

for i in range(len(forest[-1])):
    if forest[-1][i] == "#":
        Stamme_Index.append(i)


Checking_Every_Tree(forest, Stamme_Index)
