from threading import Thread, Lock

def synchronized(f):
    f.lock = Lock()
    def locker(*args, **kwargs):
        f.lock.acquire()
        f(*args, **kwargs)
        f.lock.release()
    return locker

a = 0

@synchronized
def f():
    global a
    for i in range(400000):
        a = a + 1


t = Thread(target=f)
s = Thread(target=f)

t.start()
s.start()

t.join()
s.join()

print(" *** ", a)