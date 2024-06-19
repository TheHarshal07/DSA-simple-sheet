# Here we implement the queue 

queue = []

def QueueImplementation():
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print("Initial queue ", queue)

    print("queue after pop ")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print(queue)

QueueImplementation()