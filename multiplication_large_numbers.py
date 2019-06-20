# 大数相乘
def list2str(li):
    while li[0] == 0:
        del li[0]
    res = ''
    for i in li:
        res += str(i)
    return res


def multi(a, b):
    stra = list(str(a))
    strb = list(str(b))
    lena = len(str(a))
    lenb = len(str(b))
    result = [0 for _ in range(lena + lenb)]
    for i in range(lena):
        for j in range(lenb):
            result[lena - i - 1 + lenb - j - 1] += int(stra[i]) * int(strb[j])
    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10
    return list2str(result[::-1])


if __name__ == '__main__':
    # 测试用例
    a = 123333666
    b = 456455555
    res = multi(a, b)
    print('大数相乘结果为：', res)
    print('两数直接相乘为：', a * b)
