def hanoi_solver(n):
    stacks = [[],[],[]]
    src, dest, aux = 0, 1, 2
    stacks[src] = list(range(n,0,-1))
    stacks[dest] = []
    stacks[aux] = []
    total_moves = (2 ** n) - 1
    results_str = f"{stacks[src]} {stacks[dest]} {stacks[aux]}"
    if n % 2 == 0:
        dest, aux = aux, dest
   
    
    for i in range(1,total_moves + 1):
        if i % 3 == 1:
            if (stacks[src] and (not stacks[dest] or stacks[src][-1] < stacks[dest][-1])):
                stacks[dest].append(stacks[src].pop())
            else:
                stacks[src].append(stacks[dest].pop())
        elif i % 3 == 2:
            if (stacks[src] and (not stacks[aux] or stacks[src][-1] < stacks[aux][-1])):
                stacks[aux].append(stacks[src].pop()) 
            else:
                stacks[src].append(stacks[aux].pop())
        else:
            if (stacks[dest] and (not stacks[aux] or stacks[dest][-1] < stacks[aux][-1])):
                stacks[aux].append(stacks[dest].pop())
            else:
                stacks[dest].append(stacks[aux].pop()) 
        results_str += f"\n{stacks[src]} {stacks[dest]} {stacks[aux]}" if n%2 == 0 else f"\n{stacks[src]} {stacks[aux]} {stacks[dest]}"
    return results_str
   
print(hanoi_solver(1))
print(hanoi_solver(2))
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))
