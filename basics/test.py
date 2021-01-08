class check():
    def __init__(self, a, b, c):
        print('__init__')

    @staticmethod
    def static_m():
        print("static_m")

    def member_f(self):
        print('member_m')

v = check(1, 2, 3)
v.static_m()
v.member_f()
check.static_m()
check.member_f()



