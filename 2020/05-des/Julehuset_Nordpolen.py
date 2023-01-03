
def Formatting(link):
    with open(link) as f:
        txt = f.read()
    return txt

def WalkingMap(directions: str, Map: list):
    x = 2
    y = 2
    Map[y][x] = 1
    
    for i in directions:
        if i == "H":
            x += 1
            Map[y][x] = 1
                
        elif i == "V":
            x -= 1
            Map[y][x] = 1
                
        elif i == "O":
            y += 1
            Map[y][x] = 1
            
        elif i == "N":
            y -= 1
            Map[y][x] = 1
    
    return Map

def Fill(Map):
    for i in Map:
        a = 0
        while a < len(i):
            if i[a] == 1 and i[a+1] == 0 and i[a-1] == 0:
                a += 1
                while i[a] == 0:
                    i[a] = 1
            else:
                a += 1
    
    return Map

def Area(Map: list):
    Area = 0
    for y in Map:
        for x in y:
            
            

            
    print(Area)

b = 1000
link = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\05-des\\Julehus_Rute.txt"

Map = [10*[0] for i in range(0,10)]

directions = Formatting(link)
a = "OOVVNNHH"
Map = WalkingMap("a", Map)
Map = Fill(Map)
print(Map)
# Area(Map)
