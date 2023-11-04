f = [14, 23, 37]
def replace(g):
    g = [17, 28, 45]
    print('g = ', g)

def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 19

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

replace(f)
print(f)
replace_contents(f)
print(f)
banner('hello')
banner('hello', '-')
banner('hello', border='=')
banner(border='=', message='world')
