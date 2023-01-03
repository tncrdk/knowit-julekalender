import matplotlib.pyplot as plt
import numpy as np


def Formatting(link):
    with open(link) as f:
        txt = f.read()
    return txt


link = "C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\05-des\\Julehus_Rute.txt"
string = Formatting(link)
A = []
pos = [0, 0]
for i in string:
    if i == "O":
        pos = [sum(x) for x in zip([1, 0], pos)]
        A.append(pos)
    if i == "N":
        pos = [sum(x) for x in zip([-1, 0], pos)]
        A.append(pos)
    if i == "H":
        pos = [sum(x) for x in zip([0, 1], pos)]
        A.append(pos)
    if i == "V":
        pos = [sum(x) for x in zip([0, -1], pos)]
        A.append(pos)

for i in A:
    plt.plot(i[0], i[1], "ro")
print(A)
plt.show()
""" a = 0
b = 0
for i in range(1,len(A)):
    a += A[i][0]*A[i-1][1]

for i in range(0,len(A)-1):
    b += A[i][0]*A[i+1][1]

print(abs(a-b)/2) """
