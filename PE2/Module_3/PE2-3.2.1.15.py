class QueueError(IndexError):
    pass
        
class Queue:
    def __init__(self):
        self.__stk = []

    def put(self, elem):
        self.__stk.insert(0, elem)

    def get(self):
        if self.__stk == []:
            raise QueueError
        else:
            elem = self.__stk[-1]
            del self.__stk[-1]
            return elem

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")