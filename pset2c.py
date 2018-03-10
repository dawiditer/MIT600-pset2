#Biggest Number of nuggets without a combo
def findLargestNoneCombo(pkgs):
    bestSoFar = 0
    consec = 0
    first = pkgs[0]
    second = pkgs[1]
    third = pkgs[2]
    for n in range(1, 150): 
        comboFound = False
        for a in range(int(n/first)+1):
            for b in range(int(n/second)+1):
                for c in range(int(n/third)+1):
                    if first*a + second*b + third*c == n:
                        comboFound = True
        if comboFound:
            consec += 1
        else:
            if consec != 6:
                bestSoFar = n
                consec = 0
            else:
                break
    return bestSoFar
        
def showLargestNoneCombo(pkgs):
    print "Given package sizes %i, %i and %i," %(pkgs[0],pkgs[1],pkgs[2])
    print "the largest number of McNuggets that cannot be bought"
    print "in exact quantity is: ",findLargestNoneCombo(pkgs)

packages = (3,19,30)
showLargestNoneCombo(packages)
