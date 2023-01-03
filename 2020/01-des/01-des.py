import time

start = time.time()

with open("C:\\Users\\thorb\\Documents\\Knowit-Julekalender\\01-des\\Tall.txt") as f:
    arr = f.read()
    arr = list(map(int, arr.split(",")))

arr.sort()

for i in arr:
    if i+1 != arr[i]:
        print(i+1)
        break

print(f'Total Tid {time.time()-start} sek')


# start = time.time()

# print((100000/2*100001)-sum(arr))

# tot_time = time.time() - start
# print(f'Total tid: {tot_time} sek')
