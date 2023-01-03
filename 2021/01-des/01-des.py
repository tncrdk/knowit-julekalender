numbers_to_search = [
    ("femti", 50),
    ("førti", 40),
    ("tretti", 30),
    ("tjue", 20),
    ("ti", 10),
    ("nitten", 19),
    ("atten", 18),
    ("sytten", 17),
    ("seksten", 16),
    ("femten", 15),
    ("fjorten", 14),
    ("tretten", 13),
    ("tolv", 12),
    ("elleve", 11),
    ("ni", 9),
    ("åtte", 8),
    ("sju", 7),
    ("seks", 6),
    ("fem", 5),
    ("fire", 4),
    ("tre", 3),
    ("to", 2),
    ("en", 1),
]

with open(r"tall.txt", "r", encoding="utf-8") as f:
    txt = f.read()

for i in numbers_to_search:
    txt = txt.replace(i[0], f",{i[1]}")

summen = sum([int(i) for i in txt.split(",") if bool(i)])

print(summen)
