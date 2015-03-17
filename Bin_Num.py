import math

class Bin_num(object):
    '''Superclass for Logic and Converter, this is where the binary data is stored, hopefully it can be manipulated from here too...'''
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

    def _flipbit(self, ind):
        if self.binvalue[ind] == 0:
            self.binvalue[ind] = 1
        else:
            self.binvalue[ind] = 0

    def prettyprint(self):
        if self.btype == "null":
            pass
        else:
            print str(self.decvalue), "in", str(len(self.binvalue)) + "-bit", self.HASH[self.btype] + ":"
            if self.bit % 4 == 0:
                print (("{}"*4+" ")*(self.bit/4)).format(*self.binvalue)
            else:
                print ("{}"*self.bit).format(*self.binvalue)

    def add_bin(self,bin_no):
        ''' a mathematical binary adder. Simply adds bits together and discards the carry. 
        Modifies the number, useful for adding a decimal value converted to unsigned binary to a number'''
        temp1 = self.binvalue[::-1]
        bin_no = temp2.binvalue[::-1]
        carry = 0

        for i in range(len(temp1)):
            temp1[i] += temp2[i] + carry
            if temp1[i] >= 2:
                temp1[i] += -2
                carry = 1

        self.binvalue=temp1[::-1]
        if self.btype == "uns":
            self.get_dec()

if __name__ == "__main__":
    pass
