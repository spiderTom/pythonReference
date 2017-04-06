


def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start

@coroutine
def receiver():
    print "ready to receive"
    while True:
        n = (yield )
        print "Got %s " % n

r = receiver()

r.send("1")

r.send("2")
r.send("asdfasdfasd")