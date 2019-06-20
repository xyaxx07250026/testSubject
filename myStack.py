# coding:utf8
class MyStack(object):
    def __init__(self):
        self.stack = []
        self.l_len = 0
        self.r_len = 0

    def lpush(self, x):
        temp = [x]
        self.stack = temp + self.stack
        self.l_len += 1

    def lpop(self):
        if self.lempty():
            self.l_len -= 1
            return self.stack.pop(0)
        else:
            print("The bottom of the left stack!")

    def rpush(self, x):
        self.stack.append(x)
        self.r_len += 1

    def rpop(self):
        if self.rempty():
            self.r_len -= 1
            return self.stack.pop()
        else:
            print("The bottom of the right stack!")

    def lempty(self):
        if self.l_len != 0:
            return True
        return False

    def rempty(self):
        if self.r_len != 0:
            return True
        return False


if __name__ == '__main__':
    ms = MyStack()
    # 左入栈
    ms.lpush(2)
    ms.lpush(3)
    ms.lpush(4)
    print(ms.stack)
    # 左出栈
    ms.lpop()
    ms.lpop()
    ms.lpop()
    ms.lpop()
    print(ms.stack)

    # 右入栈
    ms.rpush(2)
    ms.rpush(3)
    ms.rpush(4)
    # 右出栈
    print(ms.stack)
    ms.rpop()
    ms.rpop()
    ms.rpop()
    ms.rpop()
    print(ms.stack)
