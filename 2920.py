numbers = []
nums = input()
numbers = nums.split()
cnt = 1
num = numbers[0]
answer = "ascending"
for n in numbers:
    if cnt == 1:
        if int(n) == 8:
            answer = "descending"
    else :
        if abs(int(n) - int(num)) != 1:
            answer = "mixed"
            break
    num = n
    cnt=cnt+1

print(answer)

