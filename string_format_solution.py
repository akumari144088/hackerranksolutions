# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
revenue=0
n=int(input())
stock=list(map(int, input().split(' ')))
dict=Counter(stock)
x=int(input())
for i in range (x):
    size,price=map(int, input().split(' '))
    if(dict[size]):
       dict[size]-=1
       revenue=revenue+price
print(revenue)
