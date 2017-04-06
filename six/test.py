def outer():
    d = {'y': 0}

    def inner():
        d['y'] += 1
        return d['y']
    return inner

f = outer()
print(f(), f(), f()) #prints 1 2 3
