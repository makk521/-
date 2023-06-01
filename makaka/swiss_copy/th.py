class MyThread(threading.Thread):
    def __init__(self, params):
        pass
    def run(self):
       pass
t1 = MyThread(params)
t.setDaemon(True)
t1.start()