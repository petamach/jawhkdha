class A:

    def __init__(self):
        print("I am in a")

class B(A):
    def __init__(self):
        super().__init__()
