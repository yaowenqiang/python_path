import math
def generate(func):
    def gen_func(s):
        for item in s:
            yield func(item)

    return gen_func

def trace(source):
    for item in source:
        print(item)
        yield item

gen_sqrt = generate(math.sqrt)
for x in gen_sqrt(range(100)):
    print(x)
