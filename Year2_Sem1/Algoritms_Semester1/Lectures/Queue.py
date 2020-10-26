class QueueV1:
    def __init__(self):
        self.body = []

    def enqueue(self,element):
        self.body.append(element)

    def dequeue(self):
        print(self.body[0])
        self.body.remove([0])

    def length(self):
        return len(self.body) - self.head
    