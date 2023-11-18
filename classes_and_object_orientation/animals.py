from icecream import ic
class Animal:

    @classmethod
    def description(cls):
        return 'An animal'


class Bird(Animal):
    @classmethod
    def description(cls):
        s = super()
        print(s)
        print(s.description)
        return s.description() + ' with wings'

class Flamingo(Animal):
    @classmethod
    def description(cls):
        return super().description() + ' and fabulous pink feathers'


if __name__ == '__main__':
    ic(Animal.description())
    ic(Bird.description())
    ic(Flamingo.description())
    ic(Flamingo.__mro__)

