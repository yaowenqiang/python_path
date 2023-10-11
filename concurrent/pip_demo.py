import multiprocessing

if __name__ == '__main__':
    p1, p2 = multiprocessing.Pipe()

    cons = multiprocessing.Process(target=consumer, args=(p1, p2))

    cons.start()

    # Close the input end in the producer
    p2.close()

    # Go produce some data
    sequence = range(100)
    producer(sequence, p1)

    # Close the pipe

    p1.close()
