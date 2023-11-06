import sys

def read_series(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    try:
        #series = []
        #for line in f:
        #    a = int(line.strip())
        #    series.append(a)
        return  [int(line.strip()) for line in f]
    finally:
        f.close()

    #return series


def read_series_v2(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(sys.argv[1])
