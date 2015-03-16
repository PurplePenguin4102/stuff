class Logic(object):
    '''a subclass of Bin_num that defines all the different basic gates and combination 
    circuits that can be used.'''

    def __init__(self):
        pass

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

