class Converter(object):
    '''a class for handling conversion of Binary numbers between excess-n, 1's comp, 2's comp, sign bit binary and unsigned binary.
    Also handles addition, converting to decimal, octal and hexadecimal.'''

    def __init__(self):
        pass

    def convert_1s(self):
        self.binvalue = self.logicnot()

    def convert_2s(self):
        self.convert_1s()
        _b1 = Bin_num(1, btype=self.btype, bit=len(self.binvalue))
        self.add_bin(_b1)

    def convert_xs(self):
        pass

    def convert_sig(self):
        pass

    def get_dec(self):
        bit = len(self.binvalue)
        multiplier = 2**(bit-1)
        ans = 0
        for i in self.binvalue:
            ans += multiplier*i
            multiplier /= 2
        self.decvalue = ans

    def get_oct(self):
        pass

    def get_hex(self):
        pass

