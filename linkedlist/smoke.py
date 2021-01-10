from collections import deque

# create a linkedlist
linkedlist = deque()

#add element 
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)

print(linkedlist)

linkedlist.insert(2,99)

print(linkedlist)


# access element
e = linkedlist[2]
print(e)

# search element
index = linkedlist.index(99)
print(index)

#update
linkedlist[3] = 100
print(linkedlist)

#delete
linkedlist.remove(100) #element
print(linkedlist)
del linkedlist[2]
print(linkedlist)

#len
length = len(linkedlist)
print(length)




