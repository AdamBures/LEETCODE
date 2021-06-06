def ith(arr):
    arr2 = []
    total = 0
    for number in arr:
        total += number
        arr2.append(total)

    print(arr2)


if __name__ == "__main__":
    ith([1,2,3,4,5])
