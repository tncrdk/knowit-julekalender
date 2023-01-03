import numpy as np
import time


def FormattingGrid(link1):
    with open(link1) as f:
        arr = np.asarray(f.read().split())

    return arr


def FormattingWords(link):
    with open(link) as a:
        solutions = a.read().split()

    return solutions


def FindWordHorizontally(SearchWord, grid, FoundWord):
    for string in grid:
        if SearchWord in string:
            FoundWord.add(SearchWord)
            return FoundWord

        SearchWordTemp = SearchWord[::-1]

        if SearchWordTemp in string:
            FoundWord.add(SearchWord)
            return FoundWord


def VertiGrid(grid):
    NewGrid = []
    for column in range(len(grid)):
        NewGrid.append([i[column] for i in grid])

    return NewGrid


def FindWord(SearchWord, NewGrid, FoundWord):
    for string in NewGrid:
        if SearchWord in string:
            FoundWord.add(SearchWord)
            return FoundWord

        SearchWordTemp = SearchWord[::-1]

        if SearchWordTemp in string:
            FoundWord.add(SearchWord)
            return FoundWord


def FindWordNew(SearchWord, NewGrid, FoundWord):
    for string in NewGrid:
        Table = ""
        for i in string:
            Table = Table + i
        if SearchWord in Table:
            FoundWord.add(SearchWord)
            return FoundWord

        SearchWordTemp = SearchWord[::-1]

        if SearchWordTemp in Table:
            FoundWord.add(SearchWord)
            return FoundWord


def DiagonalGridRigth(grid):
    NewGrid = []
    for row in range(len(grid)):  # Hver rad vi skal gå gjennom som base
        TempArr = []
        y = row
        x = 0
        for dia in range(row + 1):  # Finne diagonalene
            TempArr.append(grid[y][x])
            y -= 1  # Rad
            x += 1  # Kolonne
        NewGrid.append(TempArr)

    for col in range(len(grid) - 1, 0, -1):
        TempArr = []
        y = 999
        x = len(grid) - col
        for dia in range(col):  # Finne diagonalene
            TempArr.append(grid[y][x])
            y -= 1  # Rad
            x += 1  # Kolonne
        NewGrid.append(TempArr)

    return NewGrid


def DiagonalGridleft(grid):
    NewGrid = []
    for col in range(len(grid)):
        TempArr = []
        x = col
        y = 999
        for dia in range(col + 1):
            TempArr.append(grid[y][x])
            x -= 1
            y -= 1
        NewGrid.append(TempArr)

    for row in range(len(grid) - 1, 0, -1):
        TempArr = []
        y = row
        x = 999
        for dia in range(row + 1):
            TempArr.append(grid[y][x])
            x -= 1
            y -= 1
        NewGrid.append(TempArr)

    return NewGrid


# =============================================================================
# Functions
# Execution
# =============================================================================

link1 = (
    "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\03-des\\CrossWord_Letters.txt"
)
link2 = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\03-des\\Solutions.txt"

FoundWord = {
    "rudolf",
    "mandel",
    "gløggkos",
    "julestjerne",
    "juletre",
    "jesusbarnet",
    "akevitt",
    "nordpolen",
    "medisterkake",
    "julestrømpe",
    "sølvgutt",
    "svineribbe",
    "krampus",
    "sledespor",
    "grevinne",
    "hovmester",
    "pepperkake",
    "nellik",
    "nisseverksted",
    "lutefisk",
    "adventskalender",
    "klementin",
}
grid = FormattingGrid(link1)
solutions = FormattingWords(link2)

sol = []
for i in solutions:
    if i not in FoundWord:
        sol.append(i)

sol.sort()
print(sol)
