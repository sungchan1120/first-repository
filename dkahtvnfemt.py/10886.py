V = int(input())
cute = 0

for _ in range(V):
   if int(input()) == 1:
        cute += 1

if cute > V//2:
   print("Junhee is cute!")#v나누기2를하고cute가 크면 "Junhee is cute!" 
else:
   print("Junhee is not cute!")#아니면 "Junhee is not cute!"출력
