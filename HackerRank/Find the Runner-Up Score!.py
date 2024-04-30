if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = sorted(arr)
    value = list(set(score))
    print(value[-2])
