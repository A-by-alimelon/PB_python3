n,m = map(int,input().split(' '))
numbers = list(map(int, input().split(' ')))

a,b,c = 0,1,2
answer =  0
for i in range(n-1):
    if a == b : continue
    if b == c : continue
    if c == a : continue
    if answer < (numbers[a] + numbers[b] + numbers[c]) < m :
        answer = numbers[a] + numbers[b] + numbers[c]
        print(numbers[a], numbers[b], numbers[c])
    a = a + 1
for i in range(n-2):
    if a == b : continue
    if b == c : continue
    if c == a : continue
    if answer < (numbers[a] + numbers[b] + numbers[c]) < m :
        answer = numbers[a] + numbers[b] + numbers[c]
        print(numbers[a], numbers[b], numbers[c])

    b = b + 1
for i in range(n-3):
    if a == b : continue
    if b == c : continue
    if c == a : continue
    if answer < (numbers[a] + numbers[b] + numbers[c]) < m :
        answer = numbers[a] + numbers[b] + numbers[c]
        print(numbers[a], numbers[b], numbers[c])
    c = c + 1

print(answer)