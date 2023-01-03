def Formatting(link: str):
    with open(link) as f:
        txt = f.read().replace(",", "\n").split("\n")
        txt = [i.strip() for i in txt]

    return txt


def FindAmountOfIngredient(Ingrediens: str, Leveringsliste: list):
    Sum = sum(
        [  # Comprehension
            int(i.split(" ")[1])
            for i in Leveringsliste
            if i[0 : len(Ingrediens) + 1] == Ingrediens + ":"
        ]
    )

    return Sum


def NumOfCakes(link: str, Mengdeforhold: dict):
    Leveringsliste = Formatting(link)
    Kaker = []
    Kaker.append(
        FindAmountOfIngredient("sukker", Leveringsliste) // Mengdeforhold["sukker"]
    )
    Kaker.append(
        FindAmountOfIngredient("melk", Leveringsliste) // Mengdeforhold["melk"]
    )
    Kaker.append(FindAmountOfIngredient("mel", Leveringsliste) // Mengdeforhold["mel"])
    Kaker.append(FindAmountOfIngredient("egg", Leveringsliste) // Mengdeforhold["egg"])

    print(min(Kaker))


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Python\\Knowit-Julekalender\\04-des\\Leveringsliste.txt"

Mengdeforhold = {"melk": 3, "mel": 3, "sukker": 2, "egg": 1}

NumOfCakes(link, Mengdeforhold)
