#!/usr/bin/python3

def search (arr, x, y):
    for i in range(0, x):
        if (arr[i] == y):
            return i
    return -1

def main():
    arr = [2, 3, 4, 7, 2, 4, 7]
    x = len(arr)
    y = 7
    
    result = search(arr, x, y)
    if (result == -1):
        print("no result found")
    else:
        print(f"the number is {result}")

if __name__ == "__main__":
    main()