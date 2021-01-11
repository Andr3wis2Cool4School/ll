# queue a ds that first in first out(FIFO)

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)


print(queue)


# get the head of the queue
temp1 = queue[0]
print(temp1)

# how to delete the head get out of queue

temp2 = queue.popleft()
print(queue)

print(temp2)


# queue is empty     
len(queue) == 0

# 遍历队列

while len(queue) != 0:
    temp = queue.popleft()
    print(temp)

































































