import time
while True:
    s = input()
    arr = s.split()
    if len(arr) <= 1:
        continue
    arr[0] = arr[0][:-1]
    time.sleep(0.05)
    print("_".join(arr))