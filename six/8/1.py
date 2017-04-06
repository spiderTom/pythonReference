import os
import fnmatch

def find_files(topdir, pattern):
    print "enter find_files"
    for path, dirname, filelist in os.walk(topdir):
        print path, dirname, filelist
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)

import gzip, bz2


def opener(filename):
    print "enter opener"
    for name in filename:
        print name
        if name.endswith(".gz"):
            f = gzip.open(name)
        elif name.endswith(".bz2"):
            f = bz2.BZ2File(name)
        else:
            f = open(name)
        yield f


def cat(filelist):
    print "enter cat"
    for f in filelist:
        print "f: %s " % f
        for line in f:
            print "line: %s " % line
            yield line


def grep(pattern, lines):
    print "enter grep"
    for line in lines:
        if pattern in line:
            yield line


wwwlogs = find_files("D:\SRC\Python\Github\Python Reference", "*.log")
print "===================="
files = opener(wwwlogs)
print "files: %s" % files
print "===================="
lines = cat(files)
pylines = grep("python", lines)
for line in pylines:
    sys.stdout.write(line)

