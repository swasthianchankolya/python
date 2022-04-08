class main:
    def m(self):
        print("m class")
class second(main):
    def m(self):
        super().m()
        print("second")
obj=second()
obj.m()
