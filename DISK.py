
def towerof(n,source,helper,destination):
    if n==1:
        print("Move disk 1 from",source,"to",destination)
        return

    towerof(n-1,source,destination,helper)
    print("Move disk",n,"from",source,"to",destination)
    towerof(n-1,helper,source,destination)

n=int(input("Enter number of disks:"))
towerof(n,"A","B","C")
print("Total moves:", (2**n)-1)
