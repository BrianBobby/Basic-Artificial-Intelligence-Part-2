#

def nextMove(n,r,c,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                index1=i
                index2=j
            if grid[i][j]=="m":
                index3=i
                index4=j
    for i in range(n):
        if index3>index1:
            return "UP"
            index3-=1
        elif index3<index1:
            return "DOWN"
            index3+=1
        else:
            break
    for i in range(n):
        if index4>index2:
            return "LEFT"
            index4-=1
        elif index4<index2:
            return "RIGHT"
            index4+=1
        else:
            break

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))