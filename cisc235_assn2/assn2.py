class Stack():

    def __init__(self):
        self.elements = [None] * 10
        self.t = -1

    def push(self, i):
        self.t += 1
        self.elements[self.t] = i
        if self.t == len(self.elements) - 1:
            new = [None] * len(self.elements)
            self.elements.extend(new)

    def pop(self):
        x = self.elements[self.t]
        self.t -= 1
        return x

    def isEmpty(self):
        return self.t == -1

def fun1(n):
    if n > 1:
        if n % 2 == 0:
            fun1(n // 2)
        else:
            fun1(3 * n + 1)
    print(n)

def sfun1(n):
    s = Stack()
    s.push(n)
    x = n

    while x > 1:
        if x % 2 != 0:
            x = 3 * x + 1
            s.push(x)
        else:
            x = x // 2
            s.push(x)

    while not (s.isEmpty()):
        print(s.pop())

def fun2(n):
    if n >= 6:
        fun2(n // 3)  # integer division
        fun2(2 * n // 3)  # integer division
    print(n)

def sfun2(n):
    s = Stack()
    t = Stack()
    s.push(2)
    t.push(n)
    while not s.isEmpty():
        option = s.pop()
        x = t.pop()
        if option == 2:
            while x >= 6:
                s.push(1)
                t.push(x)
                s.push(2)
                t.push(2 * x // 3)
                x = x // 3
            print(x)
        else:
            print(x)

def fun3(a, b):
    if a <= b: # a and b are integers
        m = (a + b) // 2  # integer division
        fun3(a, m - 1)
        print(m)
        fun3(m + 1, b)

def sfun3(a, b):
    s = Stack()
    b1 = b
    while a <= b:
        while a <= b1:
            m = (a + b1) // 2
            s.push(m)
            b1 = m - 1
        print(s.pop())
        a += 1
        b1 = b

def fun4(a, b): # a and b are integers
    if a <= b:
        m = (a + b) // 2 # integer division
        fun4(a, m-1)
        fun4(m+1, b)
        print(m)

def sfun4(a, b):
    t = Stack()
    s = Stack()
    i = (a, b)
    t.push(i)
    while not t.isEmpty():
        i = t.pop()
        a = i[0]
        b = i[1]
        if a <= b:
            m = (a + b) // 2
            i1 = (a, m - 1)
            i2 = (m + 1, b)
            s.push(m)
            t.push(i1)
            t.push(i2)

    while not s.isEmpty():
        print(s.pop())

def main():

    inputF1 = [7, 18, 19, 22, 105]
    print("Function 1:")
    for i in inputF1:
        print("Input Value (Recursive):", str(i))
        fun1(i)
        print("Input Value (Non-Recursive):", str(i))
        sfun1(i)

    inputF2 = [7, 18, 19, 22, 43]
    print("Function 2:")
    for i in inputF2:
        print("Input Value (Recursive):", str(i))
        fun2(i)
        print("Input Value (Non-Recursive):", str(i))
        sfun2(i)

    inputF3 = [(0, 7), (1, 18), (4, 19), (-1, 22)]
    print("Function 3:")
    for i in inputF3:
        print("Input Value (Recursive):", str(i))
        fun3(i[0], i[1])
        print("Input Value (Non-Recursive):", str(i))
        sfun3(i[0], i[1])

    inputF4 = [(0, 7), (1, 18), (4, 19), (-1, 22)]
    print("Function 4:")
    for i in inputF4:
        print("Input Value (Recursive):", str(i))
        fun4(i[0], i[1])
        print("Input Value (Non-Recursive):", str(i))
        sfun4(i[0], i[1])

main()


