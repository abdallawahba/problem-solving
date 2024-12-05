num_of_shoes = int(input())
l = []
ll = []
total_earn = 0
string_of_size = input()
l = string_of_size.split()
for i in range(len(l)):
    ll.append(int(l[i]))
num_of_customers = int(input())
for i in range(num_of_customers):
    string_of_oreder = input()
    size,price = string_of_oreder.split()
    if int(size) in ll:
        total_earn += int(price)
        ll.remove(int(size))
print(total_earn)    
