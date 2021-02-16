from Auto import Auto
class Elektriauto(Auto):
    def __init__(self, t, m, a):
        super().__init__(t, m, a)
        self.aku_suurus = 50

    def aku_kirjeldus(self):
        print("Antud aku sisaldab" + str(self.aku_suurus) + " patareid")