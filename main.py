def calculateprofit(arr,arr_size):
    profit=0
    for i in range(1,arr_size):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
prices=[800,400,700,300,900,200,500]
profit=calculateprofit(prices,len(prices))
print("max profit:",profit)