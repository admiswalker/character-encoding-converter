#import chardet


def read(path, encoding):
    with open(path, 'r', encoding=encoding) as fp:
        s = fp.read()
    return s

def write(path, s, encoding):
    with open(path, 'w', encoding=encoding) as fp:
        fp.write(s)
    return

