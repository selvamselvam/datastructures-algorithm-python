class M(object):
    def public(self):
        print("Public method")
        M._private()

    @staticmethod
    def _private():
        print("private method")


m = M()
m.public()
