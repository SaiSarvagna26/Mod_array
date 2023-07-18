A=list(map(int,input().split()))
B=int(input())
c=""

for i in A:          
    c+=str(i)
print(int(c)%B)
