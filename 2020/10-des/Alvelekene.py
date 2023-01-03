def Formatting(link):
    with open(link) as f:
        txt = f.read().split()

    txt = [i.split(",") for i in txt]

    return txt


def FindWinner(Resultatlister):
    Competitors = {}
    for lek in Resultatlister:
        for plass in range(len(lek)):
            if lek[plass] in Competitors:
                Competitors[lek[plass]] += len(lek) - plass - 1
            else:
                Competitors[lek[plass]] = len(lek) - plass - 1

    winner = ["a", 0]

    for i in Competitors:
        if Competitors[i] > winner[1]:
            winner[0] = i
            winner[1] = Competitors[i]

    print(winner)


link = "C:\\Users\\thorb\\Documents\\Python\\Knowit-Julekalender\\10-des\\Resultatlister.txt"

Resultatlister = Formatting(link)

FindWinner(Resultatlister)
