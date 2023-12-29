class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def __init__(self, x):
        super().__init__(x)  # <- не забудь!
        self.y = self.x + 5


b = B(5)
print(b.y)
