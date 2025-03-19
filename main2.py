def findwater(a,asize):
    lefttallest=[0]*asize
    righttallest=[0]*asize
    water=0
    lefttallest[0]=a[0]
    for i in range(1,asize):
        lefttallest[i]=max(lefttallest[i-1],a[i])
    righttallest[asize-1]=a[asize-1]
    for i in range(asize-2,-1,-1):
        righttallest[i]=max(righttallest[i+1],a[i])
    for i in range(0,asize):
        water+=min(lefttallest[i],righttallest[i])-a[i]
    return water
a=[0,1,2,3,2,1,2,0,1,0,2]
bars=len(a)
print("water:",findwater(a,bars))