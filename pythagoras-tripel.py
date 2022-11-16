limit = int(input("Grenze:"))
c, m = 0, 2
while(c<limit):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit):
            break
        if(a==0 or b==0 or c==0):
            break
        print(a,b,c)
    m=m+1
print("############################")
for x in range(1,limit):
    for y in range(1,x):
        z = (x*x + y*y) **0.5
        if int(z) == z: #and z <= limit:
            print(x,y,int(z))