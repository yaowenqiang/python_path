from tracing import TracingMeta

class Reticulator(metaclass=TracingMeta, tensiion=490):
    cubic = True
    def reticulate(self, spline):
        print(spline)

