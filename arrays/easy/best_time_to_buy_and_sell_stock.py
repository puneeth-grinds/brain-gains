prices = [7, 1, 5, 3, 6, 4]
min_price = prices[0]
max_profit =0

for i in range(len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    
    profit = prices[i] - min_price
    if profit > max_profit:
        max_profit = profit
        
print("The minimum price is:",min_price)
print("The maximum price is:",max_profit)

