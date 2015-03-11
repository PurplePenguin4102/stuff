import math

class Bin_num(object):

    def __init__(self, decvalue=None, binary=None, btype="uns", bit = 8):
        
        if decvalue is None:
            pass
        elif (decvalue > 2**bit) or ((btype == "uns") and (decvalue < 0)):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0
        elif (abs(decvalue) > 2**(bit-1)) and (btype != "uns"):
            print "can't do that boss"
            btype = "null"
            self.decvalue = 0
        else:
            pass

        self.HASH = {"uns":"Unsigned binary",
                     "sig":"Sign bit binary",
                     "1s":"One's complement binary",
                     "2s":"Two's complement binary",
                     "x128":"Excess 128/127 binary"}
        self.btype = btype

        if decvalue:
            self.decvalue = decvalue
            self._make_bin(bit)
            self.bit = bit
        elif binary:
            self.binvalue = binary
            self.get_dec()
            self.bit = len(binary)
        else:
            pass

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
            self.convert_2s() 
        else:
            pass

    def convert_1s(self):
        self.binvalue = self.logicnot()

    def convert_2s(self):
        self.convert_1s()
        _b1 = Bin_num(1, btype=self.btype, bit=len(self.binvalue))
        self.add_bin(_b1)

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

    def logicadd_bin(self, bin):
        "logical implementation of an unsigned adder"
        pass

    def get_dec(self):
        bit = len(self.binvalue)
        multiplier = 2**(bit-1)
        ans = 0
        for i in self.binvalue:
            ans += multiplier*i
            multiplier /= 2
        self.decvalue = ans

    def prettyprint(self):
        if self.btype == "null":
            pass
        else:
            print str(self.decvalue), "in", str(len(self.binvalue)) + "-bit", self.HASH[self.btype] + ":"
            if self.bit % 4 == 0:
                print (("{}"*4+" ")*(self.bit/4)).format(*self.binvalue)
            else:
                print ("{}"*self.bit).format(*self.binvalue)

    def logicand(self, b):
        ''' takes two binary values with the same bit and returns the bitwise logical 'and' between them. i.e. c = 1 iff a = 1 and b = 1'''
        tempbin = []
        for i in range(len(self.binvalue)):
            if self.binvalue[i] + b.binvalue[i] == 2:
                tempbin.append(1)
            else:
                tempbin.append(0)

        binary = Bin_num(binary = tempbin)
        return binary

    def logicor(self, b):
        ''' same as logicand but for or. c = 1 iff a = 1 or b = 1 '''
        tempbin = []
        for i in range(len(self.binvalue)):
            if self.binvalue[i] + b.binvalue[i] != 0:
                tempbin.append(1)
            else:
                tempbin.append(0)

        binary = Bin_num(binary = tempbin)
        return binary

    def logicnot(self):
        ''' flips all the bits of self and returns a binary'''
        tempbin = self.binvalue[:]
        for i in range(len(tempbin)):
            if tempbin[i] == 1: tempbin[i] = 0
            else: tempbin[i] = 1

        binary = Bin_num(binary = tempbin)
        return binary

    def logicnand(self, b):
        tempbin = self.logicand(b)
        binary = tempbin.logicnot()
        return binary

    def logicnor(self, b):
        tempbin = self.logicor(b)
        binary = tempbin.loginot()
        return binary

    def logicxor(self, b):
        ''' implement xor using only nand gates'''
        
        # stage 0
        in_1 = self
        in_2 = self.logicnot()
        in_3 = b
        in_4 = b.logicnot()

        # stage 1

        in_1 = in_1.logicnand(in_4)
        in_2 = in_2.logicnand(in_3)

        # stage 2

        out = in_1.logicnand(in_2)

        return out

if __name__ == "__main__":

    test1 = Bin_num(binary = [0,0,1,1])
    test2 = Bin_num(binary = [0,1,0,1])

    xor = test1.logicxor(test2)
    xor.prettyprint()
    # b1 = Bin_num(11, bit = 8)
    # notb1 = b1.logicnot()
    # nothing = b1.logicand(notb1)
    # everything = b1.logicor(notb1)

    # nothing.prettyprint()
    # everything.prettyprint()