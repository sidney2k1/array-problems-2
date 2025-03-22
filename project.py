a=[1,4,2,65,45,87,34,87,89]
smallest=a[0]
largest=a[1]
for i in range(0,len(a)):
    if a[i]>largest:
        largest=a[i]
    elif a[i]==largest:
        largest==a[i]
    else:
        if smallest>a[i]:
            smallest=a[i]
        else:
            pass
sum=largest-smallest
print(sum)