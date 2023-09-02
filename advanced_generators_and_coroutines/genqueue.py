def sendto_queue(source, thequeue):
    for item in source:
        for item in source:
            thequeue.put(item)

    thequeue.put(StopIteration)
