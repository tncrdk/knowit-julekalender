
with open("C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\01-des\\Tall.txt") as f:
    arr = set(map(int, f.read().split(",")))

print(set(range(1, 100000)) - arr)