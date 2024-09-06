try:
    h=int(input("Enter a height : "))
    lb=0
    ub=(h*2)-1
    for i in range(0,h*2):
        for j in range(0,h*2):
            if j>=lb and j<=ub:
                if i<h:
                    print((h-(i%h)),end="")
                else:
                    print((h-((h-1-i)%h)),end="")
            elif j<lb:
                print((h-(j%h)),end="")
            elif j>ub:
                print((h-((h-1-j)%h)),end="")
        if i<h:
            lb+=1
            ub-=1
        else:
            lb-=1
            ub+=1
        print()
except:
    print("ERROR")
