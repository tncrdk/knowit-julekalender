
def Formatting(link):
    Dict = {}
    with open(link) as f:
        txt = f.read().split("\n")
    
    PreDict = [i.split(": ") for i in txt[0:50]]
    Dict = {}
    Dict.update({i[0]: {"Coordinates": list(map(int, i[1].replace("(", "").replace(")", "").split(","))), "Time": 0} for i in PreDict})
    Destinations = txt[50:]
    
    return Dict, Destinations


def TimeDelay(x: int, y: int, Dict: dict):
    for i in Dict:
        Distance = abs(Dict[i]["Coordinates"][0] - x) + abs(Dict[i]["Coordinates"][1] - y)
        
        if Distance == 0:
            continue
        elif Distance < 5:
            Dict[i]["Time"] += 0.25
        elif Distance < 20:
            Dict[i]["Time"] += 0.5
        elif Distance < 50:
            Dict[i]["Time"] += 0.75
        else:
            Dict[i]["Time"] += 1
    
    return Dict


def PathFindingTwoPoints(x: int, y: int, Destination: str, Dict: dict):
    x_goal = Dict[Destination]["Coordinates"][0]
    if x_goal - x != 0:    
        x_diff = x_goal - x
        Increment = x_diff/abs(x_diff)
    
    Steps = []
    
    while x != x_goal:
        Steps.append((x, y))
        x += Increment
    
    y_goal = Dict[Destination]["Coordinates"][1]
    
    if y_goal - y != 0:    
        y_diff = y_goal - y
        Increment = y_diff/abs(y_diff)
    
    while y != y_goal:
        Steps.append((x, y))
        y += Increment
    
    return Steps


def TotalPath(Dict, Destinations):
    x = 0
    y = 0
    Total_Steps = []
    
    for destination in Destinations:
        Total_Steps += PathFindingTwoPoints(x, y, destination, Dict)
        x, y = Dict[destination]["Coordinates"]
    
    Total_Steps += [Dict[Destinations[-1]]["Coordinates"]]
        
    return Total_Steps


def TimeDifference(Dict, Destinations):
    Total_Steps = TotalPath(Dict, Destinations)
    
    for i in Total_Steps:
        Dict = TimeDelay(i[0], i[1], Dict)
    
    Delays = [i["Time"] for i in Dict.values()]
    
    print(max(Delays) - min(Delays))


# =============================================================================
# Functions
# Execution
# =============================================================================

link = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\08-des\\Santa_Route.txt"

Dict, Destinations = Formatting(link)


TimeDifference(Dict, Destinations)






