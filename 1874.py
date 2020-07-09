class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

stack1 = Stack()
n = int(input())
idx = 0
numbers = list(range(1,n+1))
seq = []
for i in range(n):
    num = int(input())
    seq.append(num)
for i in seq:

    if idx < n:
        while numbers[idx] <= i:
            stack1.push(numbers[idx])
            print('+')
            idx = idx+1
            if idx >= n:
                break
            #print("idx : ", idx)
    if stack1.pop() == i:
        print('-')
    else:
        print('NO')
        break




