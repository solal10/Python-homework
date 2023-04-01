def moshe(c, n):
    result = [0]
    for i in range(n):
        result.append([c[i], i + 1])
    for i in range(1, n + 1):
        for j in range(1, i):
            temp = result[j][0] + result[i - j][0]
            if temp > result[i][0]:
                result[i][0] = temp
                result[i][1] = [result[j][1], result[i - j][1]]
    return result


print(moshe([4, 20, 1, 37, 5, 10], 6))
