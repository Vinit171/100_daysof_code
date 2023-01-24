a = list(map(int,input().split()))
b = int(input())

min_price=100000
profit = 0
for m in a:
    min_price = min(min_price,m)
    profit = max(profit,m-min_price)
    #print(min_price,"min")
    #print(profit,"Sdfsf")

print(profit)