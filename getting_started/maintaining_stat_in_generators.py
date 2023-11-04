def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [13,6,6,2,1,1]
    #for item in take(3, distinct(items)):
    for item in take(3, list(distinct(items))): # convert generator to list for easy debug
        print(item)


def main():
    run_pipeline()

if __name__ == '__main__':
    main()
