import sys

def beautifulDays(i, j, k):
    # Complete this function
    bDay = []
    for day in range(i,j+1):
        rvint=int(''.join(reversed(str(day))))
        if (rvint-day)%k == 0 :
            bDay.append(day)
    return len(bDay)

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
