def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    print(last_letter)
    return sorted(strings, key=last_letter)

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l)
    inner()

def enclosing():
    def local_func():
        print('local func')
    return local_func

print(sort_by_last_letter(['hello', 'from', 'a ','local','function']))


lf = enclosing()
lf()

