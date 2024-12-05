digits = input()
i=0
while(digits[i+1] != " "):
    i+=1
a = int(digits[0:i+1])%100
j=i
while(digits[j+1] != " "):
    j+=1
b = int(digits[i+2:j+1])%100
k=j
while(digits[k+1] != " "):
    k+=1
c = int(digits[j+2:k+1])%100
l=k
while(digits[l+1] != " "):
    l+=1
d = int(digits[k+2:l+1])%100
z = (a * b * c * d)%100
if(z<10):
    print("0" + z)
else:
    print(z)