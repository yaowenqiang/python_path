def sequence_class(immutable):
    #if immutable:
    #    cls = tuple
    #else:
    #    cls = list
    return tuple if immutable else list
    #return cls
