
enable_traceing = True

if enable_traceing:
    debug_log = open("debug.log", "w")

def trace(func):
    if enable_traceing:
        print "enter trace's enable_traceing"
        def callf(*args, **kwargs):
            print "enter callf"
            debug_log.write("Calling %s: %s, %s\n" %
                            (func.__name__, args, kwargs))
            print ("Calling %s: %s, %s\n" %
                            (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            debug_log.write("%s returned %s\n" % (func.__name__, r))
            print ("%s returned %s\n" % (func.__name__, r))
            return r
        return callf
    else:
        return func

def testf(a, b):
    return a + b

if __name__ == "__main__":
    print "main"
    print "before trace!!!!"
    result = trace(testf)
    print "after trace!!!"
    print result(1,2)

