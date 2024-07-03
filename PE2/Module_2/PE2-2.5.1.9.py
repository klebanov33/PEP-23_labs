Birthday = input("Enter birthday number in one of te following formats (YYYYMMDD, YYYYDDMM, MMDDYYYY): ")

BrStr = Birthday
sumN = 0

while len(BrStr) != 1:
    for i in BrStr:
        sumN += int(i)
    BrStr = str(sumN)
    sumN = 0

print(BrStr)        