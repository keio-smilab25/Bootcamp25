a, b = input().split()

def multiply(x, y):
    return x * y

def main():
    result = multiply(int(a), int(b))
    if result % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()
