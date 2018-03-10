#McNuggets
#6a + 9b + 20c = n
#Assumptions:
#   a <= int(n/6), b <= int(n/9) c = int(n/20)
def mcNuggets(n):
    comboFound = False
    print "\n",n,"Nuggets: "
    print "-"*31,"\n6Packs\t9Packs\t20Packs\n","-"*31
    for a in xrange(int(n/6)+1):
        for b in xrange(int(n/9)+1):
            for c in xrange(int(n/20)+1):
                if (6*a) + (9*b) + (20*c) == n:
                    print a,"\t",b,"\t",c,"\t"
                    comboFound = True
    if not comboFound:
        print "None\tNone\tNone"
                    
    
    print
##mcNuggets(127)
##mcNuggets(43)
for i in xrange(50,66):
    mcNuggets(i)
