import math

class Bin_num(object):

    def __init__(self, decvalue, btype="uns", bit = 8):
        
        if (decvalue > 2**bit) or ((btype == "uns") and (decvalue < 0)):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0
        elif (abs(decvalue) > 2**(bit-1)) and (btype != "uns"):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0

        self.HASH = {"uns":"Unsigned binary",
                     "sig":"Sign bit binary",
                     "1s":"One's complement binary",
                     "2s":"Two's complement binary",
                     "x128":"Excess 128/127 binary"}
        self.btype = btype
        self.decvalue = decvalue
        self._make_bin(bit)
        
    def _make_bin(self,bit):

        position = []
        tempvalue = abs(self.decvalue)
        for i in range(bit):
            position.insert(0, tempvalue % 2)
            tempvalue /= 2

        self.binvalue = position

        if (self.decvalue < 0) and (self.btype == "sig"):
            position[0] = 1
        elif (self.decvalue < 0) and (self.btype == "1s"):
            self.convert_1s()
        elif (self.decvalue < 0) and (self.btype == "2s"):
            self.convert_1s()            
            _b1 = Bin_num(1,btype = self.btype, bit=len(position))
            self.add_bin(_b1)

    def convert_1s(self):
        position = self.binvalue
        for i in position:
            if i: i = 0
            else: i = 1

        self.binvalue = position

    def add_bin(self,bin_no):
        temp1 = self.binvalue[::-1]
        temp2 = bin_no.binvalue[::-1]
        carry = 0

        for i in range(len(temp1)):
            temp1[i] += temp2[i] + carry
            if temp1[i] >= 2:
                temp1[i] += -2
                carry = 1

        self.binvalue=temp1[::-1]
        if self.btype == "uns":
            self.get_dec()

    def get_dec(self):
        bit = len(self.binvalue)
        multiplier = 2**(bit-1)
        ans = 0
        for i in self.binvalue:
            ans += multiplier*i
            multiplier /= 2
        self.decvalue = ans

    def prettyprint(self,bit):
        if self.btype == "null":
            pass
        else:
            print str(self.decvalue), "in", str(len(self.binvalue)) + "-bit", self.HASH[self.btype] + ":"
            if bit % 4 == 0:
                print (("{}"*4+" ")*(bit/4)).format(*self.binvalue)
            else:
                print ("{}"*bit).format(*self.binvalue)

if __name__ == "__main__":

    b1 = Bin_num(11, bit=8)
    b2 = Bin_num(125, btype = "uns", bit=8)
    # b3 = Bin_num(-125, btype = "2s", bit=8)

    b1.prettyprint(8)
    # b_2.prettyprint(8)
    b2.prettyprint(8)
    # b3.prettyprint(8)

    b1.add_bin(b2)
    b1.prettyprint(8)

    print -128 + 64 + 32 + 16 + 4 + 1