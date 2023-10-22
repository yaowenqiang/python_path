class ChessCoordinate:
    # def __new__(cls, *args, **kwargs):
    def __new__(cls, file, rank):
        # print(f'cls = {cls.__name__}')
        # print(f'args = {args!r}')
        # print(f'kwargs = {kwargs!r}')
        obj = object.__new__(cls)
        # print(f'id(obj) = {id(obj)}')
        return obj

    def __init__(self, file, rank):
        # print(f'id(self) = {id(self)}')
        instance_dictionary = self.__dict__
        if len(file) != 1:
            raise ValueError(
                f'{type(self).__name} component file {file!r}'
                f'does not have a length of one.'
            )

        if file not in 'abcdefgh':
            raise ValueError(
                f'{type(self).__name} component file {file!r}'
                f'is out of range.'
            )

        if rank not in range(1, 9):
            raise ValueError(
                f'{type(self).__name} component rank {rank | r}'
                f'is out of range.'
            )

        self._file = file
        self._rank = rank

    @property
    def rank(self):
        return self._rank

    @property
    def file(self):
        return self._file

    def __repr__(self):
        return f'{type(self).__name__}(file={self.file}, rank={self.rank})'

    def __str__(self):
        return f'{self.file}{self.rank}'


def main():
    #white_queue = ChessCoordinate('d', 4)
    #print(white_queue)
    import tracemalloc
    tracemalloc.start()
    boards = [starting_board() for _ in range(10000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    peak_kb = peak / 10 ** 3
    print(f'peak memory usage: {peak_kb} KB')

def starting_board():
    return {
        '♕♖': ChessCoordinate('a', 1),
        '♕♘': ChessCoordinate('b', 1),
        '♕♙': ChessCoordinate('c', 1),
        '♕♕': ChessCoordinate('d', 1),
        '♔♔': ChessCoordinate('e', 1),
        '♔♙': ChessCoordinate('f', 1),
        '♔♘': ChessCoordinate('g', 1),
        '♔♖': ChessCoordinate('h', 1),
    }


if __name__ == '__main__':
    main()
