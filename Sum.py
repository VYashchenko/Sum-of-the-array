sum = 0
listData = [12, 13, 0, 12, 144]

for i in range(len(listData)):
    sum = sum + listData[i]

order = "The sum of the array is {}"
print(order.format(sum))