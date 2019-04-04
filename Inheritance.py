#Inheritance-single-normal
"""class a:
    def f1(self):
        print('One')
    def f2(self):
        print('Two')
    def f3(self):
        print('Three')
class b(a):
    def f4(self):
        print('Four')
    def f5(self):
        print('Five')
    def f6(self):
        print('Six')"""
#Inheritance-single-overriding
"""class a:
    def f1(self):
        print('aF1')
    def f2(self):
        print('aF2')
    def f3(self):
        print('aF3')
class b(a):
    def f1(self):
        super().f2()
        print('bF1')
    def f2(self):
        print('bF2')
    def f3(self):
        print('bF3')"""
#Inheritance-multilevel
"""class a:
    def f1(self):
        print('One')
    def f2(self):
        print('Two')
    def f3(self):
        print('Three')
class b(a):
    def f4(self):
        print('Four')
    def f5(self):
        print('Five')
    def f6(self):
        print('Six')
class c(b):
    def f7(self):
        print('Seven')
    def f8(self):
        print('Eight')
    def f9(self):
        print('Nine')"""
#Inheritance-multilevel-overriding
"""class a:
    def f1(self):
        print('aF1')
    def f2(self):
        print('aF2')
    def f3(self):
        print('aF3')
class b(a):
    def f1(self):
        super().f1()
        print('bF1')
    def f2(self):
        print('bF2')
    def f3(self):
        print('bF3')
class c(b):
    def f1(self):
        super().f1()
        print('cF1')
    def f2(self):
        print('cF2')
    def f3(self):
        print('cF3')"""
#Inheritance-multiple-normal
"""class a:
    def f1(self):
        print('One')
    def f2(self):
        print('Two')
    def f3(self):
        print('Three')
class b:
    def f4(self):
        print('Four')
    def f5(self):
        print('Five')
    def f6(self):
        print('Six')
class c(a,b):
    def f7(self):
        print('Seven')
    def f8(self):
        print('Eight')
    def f9(self):
        print('Nine')"""
#Inheritance-multiple-overriding
"""class a:
    def f1(self):
        print('aF1')
    def f2(self):
        print('aF2')
    def f3(self):
        print('aF3')
class b:
    def f1(self):
        
        print('bF1')
    def f2(self):
        print('bF2')
    def f3(self):
        print('bF3')
class c(b,a):
    def f1(self):
        super().f1()
        print('cF1')
    def f2(self):
        print('cF2')
    def f3(self):
        print('cF3')"""
#Inheritance-hierarchical
class a:
    def f1(self):
        print('One')
    def f2(self):
        print('Two')
    def f3(self):
        print('Three')
class b(a):
    def f4(self):
        print('Four')
    def f5(self):
        print('Five')
    def f6(self):
        print('Six')
class c(a):
    def f7(self):
        print('Seven')
    def f8(self):
        print('Eight')
    def f9(self):
        print('Nine')
#Assignment
'''class a:
    def test(self):
        print('A')
class b(a):
    def test(self):
        print('B')
class c(a):
    def test(self):
        print('C')
class d(a):
    def test(self):
        print('D')'''



