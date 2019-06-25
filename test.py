
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
values = [9, 11, 13]
print(list(i for i in range(0, len(mylist)) if mylist[i] in values))