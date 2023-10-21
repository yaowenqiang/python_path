class ChessCoordinate:
    def __new__(cls, *args, **kwargs):
        print(f'cls = {cls.__name__}')
        print(f'args = {args!r}')
        print(f'kwargs = {kwargs!r}')
        obj = object.__new__(cls)
        print(f'id(obj) = {id(obj)}')
        return obj

    def __init__(self, file, rank):
        print(f'id(self) = {id(self)}')
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
    white_queue = ChessCoordinate('d', 4)
    print(white_queue)


if __name__ == '__main__':
    main()
