test_case = int(input())
for _ in range(test_case):
    cursor = 0
    pw = list(input())
    answer = []
    #print(pw)
    while pw:
        #print(pw[0])
        if pw[0] == '<':
            if cursor == 0:
                pass
            else:
                cursor -= 1
            pw.pop(0)
            #print("cursor : ", cursor)
        elif pw[0] == '>':
            if cursor == len(answer):
                pass
            else:
                cursor += 1
            #print("cursor : ", cursor)
            pw.pop(0)
        elif pw[0] == '-':
            if cursor > 0:
                del answer[cursor-1]
                cursor -= 1
            pw.pop(0)
        else:
            answer.insert(cursor,pw.pop(0))
            #print("answer :" , answer)
            cursor += 1
    print("".join(answer))

