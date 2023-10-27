class PhaseMeta(type):
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        obj._pre_init(*args, **kwargs)
        obj.__init(*args, **kwargs)
        obj._post_init(*args, **kwargs)
        return obj
class PhasedInit(metaclass=PhaseMeta):
    # def __init__(self):
    #     self._pre_init()
    #     self._do_init()
    #     self._post_init()

    def _pre_init(self):
        print('Pre-initialization')

    # def _do_init(self):
    #     print('Initialization')
    def _init__(self):
        print('Initialization')

    def _post_init(self):
        print('Post-initialization')


class SubPhaseInit(PhasedInit):
    def _do_init(self):
        print('Sub-phase initialization')


if __name__ == '__main__':
    p = PhasedInit()
    print(p)

    s = SubPhaseInit()
    print(s)

