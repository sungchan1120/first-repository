a="4546793"
b=[]

for i in range(0,len(a)-1):
    if (int(a[i])%2==0 and int(a[i+1])%2==0) : #짝수연속
        b.append(a[i]+"*")


    elif (int(a[i])%2==1 and int(a[i+1])%2==1) : #홀수연속
        b.append(a[i]+"-")

    else :
        b.append(a[i])

print("".join(b)+a[len(a)-1])
