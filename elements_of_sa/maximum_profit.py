# price of share at start of day
S = [10, 2, 3, 10, 9, 8, 12, 4, 5, 20]

# compute max profit that can be made. buys and sell have to start at begin of day

# Big(O) --> O(n^2)

max_profit = 0

for i, value in enumerate(S):
    for j in range(i, len(S)):
        buy_price = S[i]
        sell_price = S[j]
        profit = sell_price - buy_price
        if profit < 0:
            continue
        if profit > max_profit:
            max_profit = profit

print(max_profit)



