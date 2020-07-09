test_case = int(input())
friends = int(input())
for _ in range(test_case):
    network = []
    for f in range(friends):
        f1, f2 = {input().split(' ')}
        if f1 not in network:
            f1['leader'] = f1
            f2['leader'] = f2
            network.append(f1)
            



