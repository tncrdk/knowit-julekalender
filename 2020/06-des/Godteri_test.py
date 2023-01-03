link = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\06-des\\Godteri.txt"

with open(link) as f:
    txt = f.read().split(",")

Godteri = [int(i) for i in txt]
Liste_med_Godteri = []
Sum = 0
for i in Godteri:
    Sum += i
    if Sum % 127 == 0:
        Liste_med_Godteri.append(Sum/127)

print(max(Liste_med_Godteri))