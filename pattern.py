def pattern1(h):
# *
# **
# ***
# ****
    if h<1:
        print("Invalid height")
        return
    for i in range(h):
        print("*"*(i+1))

def pattern2(h):
# 1
# 23
# 456
# 78910
    if h<1:
        print("Invalid height")
        return
    term=1
    for i in range(h):
        for j in range(i+1):
            print(term,"\t",end="")
            term+=1
        print()

def pattern3(h):
# 1
# 12
# 123
# 1234
    if h<1:
        print("Invalid height")
    for i in range(1,h+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
def pattern3_2(h):
# 1
# 12
# 123
# 1234
    if h<1:
        print("Invalid height")
    for i in range(1,h+1):
        print(*range(1,i+1),sep=" ")

def pattern4(h):
#    *
#   **
#  ***
# ****
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        print("*"*(i+1))
def pattern5(h):
#    *
#   **
#  ***
# ****
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        print("* "*(i+1))

def pattern6(h):
#      1
#     12
#    123
#   1234
#  12345
# 123456
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        for j in range(1,(i+2)):
            print(j,end="")
        print()

def pattern7(h):
#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  1 2 3 4 5 
# 1 2 3 4 5 6 
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        for j in range(1,(i+2)):
            print(j,"",end="")
        print()

def pattern8(h):
# 1
# 21
# 321
# 4321
# 54321
# 654321
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        for j in range(i+1,0,-1):
            print(j,end="")
        print()
def pattern9(h):
#      1
#     21
#    321
#   4321
#  54321
# 654321
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        for j in range(i+1,0,-1):
            print(j,end="")
        print()
def pattern10(h):
#      1 
#     2 1 
#    3 2 1 
#   4 3 2 1 
#  5 4 3 2 1 
# 6 5 4 3 2 1 
    if h<1:
        print("Invalid height")
    for i in range(0,h):
        print(" "*(h-i-1),end="")
        for j in range(i+1,0,-1):
            print(j,"",end="")
        print()

def pattern11(h):
# 15    14	13	12	11	
# 10	9	8	7	
# 6	    5	4	
# 3	    2	
# 1
    c=(h*(h+1))//2
    for i in range(0,h):
        for j in range(h,i,-1):
            print(c,"\t",end="")
            c-=1
        print()
def pattern12(h):
# 15	14	13	12	11	
#  	    10	9	8	7	
#  	 	    6	5	4	
#  	 	 	    3	2	
#  	 	 	 	    1	
    c=(h*(h+1))//2
    for i in range(0,h):
        print("\t"*(i),end="")
        for j in range(h,i,-1):
            print(c,"\t",end="")
            c-=1
        print()
def pattern13(h):
# 15	14	13	12	11	
#  	 10	9	8	7	
#  	 	 6	5	4	
#  	 	  3	2	
#  	 	    1	
    c=(h*(h+1))//2
    for i in range(0,h):
        print(" "*(i),end="")
        for j in range(h,i,-1):
            print(c,"",end="")
            c-=1
        print()

def pattern14(h):
    #pascal triangle
    if h<1:
        print("Invalid height")
    else:
        for i in range(1,h+1):
            term=1
            for j in range(1,i+1):
                print(term,end=" ")
                term=int(term*((i-j)/j))
            print()

def pattern15(h):
    #pascal triangle
    if h<1:
        print("Invalid height")
    else:
        for i in range(1,h+1):
            print(" "*(h-i),end=" ")
            term=1
            for j in range(1,i+1):
                print(term,end="")
                term=int(term*((i-j)/j))
            print()
def pattern16(h):
    #pascal triangle
    if h<1:
        print("Invalid height")
    else:
        for i in range(1,h+1):
            print(" "*(h-i),end=" ")
            term=1
            for j in range(1,i+1):
                print(term,"",end="")
                term=int(term*((i-j)/j))
            print()
def pattern17(h):
    #pascal triangle
    if h<1:
        print("Invalid height")
    else:
        for i in range(h,0,-1):
            print(" "*(h-i),end=" ")
            term=1
            for j in range(1,i+1):
                print(term,"",end="")
                term=int(term*((i-j)/j))
            print()

def pattern18(h):
#diamond star
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
    if h<1:
        print("Invalid height")
    else:
        for i in range(1,h+1):
            print(" "*(h-i),end="")
            print("* "*i)
        for i in range(h-1,0,-1):
            print(" "*(h-i),end="")
            print("* "*i)

def pattern19(h):
#diamond star
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
    if h<1 or h%2==0:
        print("Invalid height")
    else:
        h=(h//2)+1
        for i in range(1,h+1):
            print(" "*(h-i),end="")
            print("* "*i)
        for i in range(h-1,0,-1):
            print(" "*(h-i),end="")
            print("* "*i)

def pattern20(h):
#5555555555
#5444444445
#5433333345
#5432222345
#5432112345
#5432112345
#5432222345
#5433333345
#5444444445
#5555555555
    if h<1:
        print("Invalid height")
        return
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

def execute(h):
    print("PATTERN 1:\n")
    pattern1(h)
    print("PATTERN 2:\n")
    pattern2(h)
    print("PATTERN 3:\n")
    pattern3(h)
    print("PATTERN 3_2:\n")
    pattern3_2(h)
    print("PATTERN 4:\n")
    pattern4(h)
    print("PATTERN 5:\n")
    pattern5(h)
    print("PATTERN 6:\n")
    pattern6(h)
    print("PATTERN 7:\n")
    pattern7(h)
    print("PATTERN 8:\n")
    pattern8(h)
    print("PATTERN 9:\n")
    pattern9(h)
    print("PATTERN 10:\n")
    pattern10(h)
    print("PATTERN 11:\n")
    pattern11(h)
    print("PATTERN 12:\n")
    pattern12(h)
    print("PATTERN 13:\n")
    pattern13(h)
    print("PATTERN 14:\n")
    pattern14(h)
    print("PATTERN 15:\n")
    pattern15(h)
    print("PATTERN 16:\n")
    pattern16(h)
    print("PATTERN 17:\n")
    pattern17(h)
    print("PATTERN 18:\n")
    pattern18(h)
    print("PATTERN 19:\n")
    pattern19(h)
    print("PATTERN 20:\n")
    pattern20(h)

try:
    n=int(input("Enter height : "))
    execute(n)
except:
    print("ERROR : ONLY INTEGER INPUT ACCEPTED")
