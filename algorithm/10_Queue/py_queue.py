from collections import deque
# from queue import Queue, PriorityQueue
# from heapq import heappop, heappush

# queue = []
# queue.append('A')
# queue.append('B')
# print(queue)
# print(queue.pop(0))
# print(queue)

queue = deque()
print(type(queue)) # instance
queue.append('A')
queue.append('B')
print(queue)
print(queue.popleft())
print(queue)


queue = Queue(maxsize=3)
queue.put('A')
queue.put('A')
queue.put('A')
queue.put('A')

print(queue.get())
print(queue.maxsize)