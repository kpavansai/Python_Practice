from threading import Thread


class myThread(Thread):
    def __init__(self, threadID):
        Thread.__init__(self)
        self.id = threadID

    def run(self):
        for _ in range(50):
            for j in range(self.id):
                print("     ", end=" ")
            print(self.id)


for i in range(10):
    myThread(i).start()
