
n = 10
class countdown(object):
    def __init__(self, param):
        self.n = param

    def next(self):
        r = self.n
        self.n -= 1
        return r


def outer():
    d = {'y': 0}

    def inner():
        d['y'] += 1
        return d['y']
    return inner

'''
def testfunc(n):
    def next():
        r = n
        n -= 1
        return r
    return next

testnext = testfunc(4)
while True:
    v = testnext()
    print "in testfunc: %d" % v
    if not v: break
'''



c = countdown(10)
while True:
    v = c.next()
    print v
    if not v: break
