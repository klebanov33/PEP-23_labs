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
    
    def get_stk_status(self):
        return self.__stk

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        queue_status = True
        if Queue.get_stk_status(self) == []:
            queue_status = True
        else:
            queue_status = False
        return queue_status

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")