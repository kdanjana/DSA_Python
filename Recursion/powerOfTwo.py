def pow(n):
    if n == 1:
        return True
    if n == 0:
        return False
    if n % 2 != 0:  #if n is odd
        return False
    return pow(n // 2)

if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(pow(n))