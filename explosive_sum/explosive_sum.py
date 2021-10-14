def exp_sum(n: int) -> int:
    cache = [0] * (n + 1)
    cache[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            cache[j] += cache[j-i]
    return cache[n]+1


if __name__ == '__main__':
    print(exp_sum(1))  # 1
    print(exp_sum(2))  # 2  -> 1+1 , 2
    print(exp_sum(3))  # 3 -> 1+1+1, 1+2, 3
    print(exp_sum(4))  # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
    print(exp_sum(5))  # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
    print(exp_sum(10))  # 42
    print(exp_sum(50))  # 204226
    print(exp_sum(80))  # 15796476
    print(exp_sum(100))  # 190569292
