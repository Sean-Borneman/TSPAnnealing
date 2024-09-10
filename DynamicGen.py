import math


fullEq = ""
n = 4
file1 = open("QUBOcities" + str(n) + ".txt","a") 
def x(i, j):
    return "x_" + str(i*n+j+1)
def h1():
    eq = ""
    # eq += "("
    for j in range(n):
        if j != 0:
            eq += "+(1-(" # currently triggers before anything else is there :)
        else:
            eq += "(1-("
        for i in range(n):
            eq+="+"+x(i, j)
        eq+="))^2"
    # eq += "))"
    return eq
def h2():
    eq = ""
    # eq += "("
    for i in range(n):
        if i != 0:
            eq += "+(1-(" # currently triggers before anything else is there :)
        else:
            eq += "(1-("
        for j in range(n):
            eq+="+"+x(i, j)
        eq+="))^2"
    # eq += "))"
    return eq
def r(origin, j ,k):
    # print("triggered" + str(k) +"|" + str(n/2))
    if k >(n/2):
        return "1"
    else:
        tempString = x(j, origin)
        for m in range(n):
            tempString += "+"+x(j,m) + "*(" + r(origin, m, k+1) +")"
       
    return tempString
def h3():
    eq = ""
    for i in range(n):
        for j in range(n):
            eq += '+'+x(i, j)+"*(" + r(i,j,1)+")"
            #print('+'+x(i, j)+"*(" + r(i,j,1)+")")

    return eq
#fullEq += h1() +"+"+ h2() +"+"+ h3() 
#print(fullEq)
print(h1() + "")
print("-------------------------------------------------------")
print(str(h2()))
print("-------------------------------------------------------")
open("QUBOcities" + str(n) + ".txt", "w").writelines(h3())