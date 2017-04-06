import time

def tail(f):
    #f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line


wwwlog = tail(open("1.txt"))
print wwwlog
print "=============="
pylines = grep(wwwlog, "python")
print "--------------"
print pylines
for line in pylines:
    print line
