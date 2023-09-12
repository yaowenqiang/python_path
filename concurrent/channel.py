import pickle

class Channel(object):
    def __init__(self, out_f, in_f):
        self.out_f = out_f
        self.in_f = in_f

    def send(self, item):
        pickle.dump(item, self.out_f)
        self.out_f.flush()
    def rece(self):
        return pickle.load(self.in_f)

