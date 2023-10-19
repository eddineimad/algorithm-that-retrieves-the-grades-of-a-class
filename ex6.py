t1=[]
t=[]
n=int(input("Type the number of students :"))
for i in range (0,n) :
    m=int(input("Type the grade "))
    while m<0 or m>20 :
       M=int(input("Type in grade number between 0 and 20 "))
    t1.append(M)
    s=0
S=S+M
e=S/n
for i in range (0,n) :
    if t1[i]>e :
        t.append(t1[i])
print("Grades higher than averge are :",t)