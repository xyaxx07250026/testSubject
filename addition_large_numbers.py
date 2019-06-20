# 模拟实现大数相加
def addNums(num1, num2):
    num1 = str(num1)[::-1]
    num2 = str(num2)[::-1]
    len1, len2 = len(num1), len(num2)
    max = len1 if len1 > len2 else len2
    sum = ''
    carry = 0
    for i in range(max):
        fir = int(num1[i]) if i < len1 else 0
        sec = int(num2[i]) if i < len2 else 0
        add = (fir + sec + carry) % 10
        carry = int((fir + sec + carry) / 10)
        sum += str(add)
    if carry > 0:
        sum += str(carry)
    if sum == '':
        print(0)
    print(sum[::-1])


if __name__ == '__main__':
    # 测试用例1
    # num1 = 0
    # num2 = 0
    # 测试用例2
    # num1 = 0
    # num2 = 432456778
    # 测试用例3
    # num1 = 123456787
    # num2 = 0
    # 测试用例4
    num1 = 123456787
    num2 = 432456778
    addNums(num1, num2)
