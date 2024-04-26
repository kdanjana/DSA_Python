def isPowerTwo(n):
    count = 0
    while n > 0:
        if n & 1 == 1:     #set bits counting
            count += 1
        n = n >> 1
    if count == 1:
        return True
    return False

if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(isPowerTwo(n))