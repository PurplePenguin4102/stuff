class Combinations(object):
    ''' a class for dealing with combinational logic: Adders, decoders, multiplexers. To be used with Bin_nums'''

    def __init__(self):
        pass
        
    def onebit_adder(self, bin, carry):
        "logical implementation of an unsigned adder"
        if not ((self.bit, bin.bit, carry.bit) == (1, 1, 1)):
            print "Did nothing, numbers weren't 1 bit"
            return
        else:
            #stage 1
            spart = self.logicxor(bin)
            cout1 = self.logicand(bin)

            #stage 2
            s = spart.logicxor(carry)
            cout2 = spart.logicand(carry)

            #stage 3
            carry_out = cout1.logicor(cout2)

            return (s,carry_out)

    def nbit_adder(self, bin):
        if self.bit != bin.bit:
            print "numbers must be the same bit"
            return
        else:
            carry = Bin_num(binary = [0])
            n = self.bit
            ans = []
            for i in range(n)[::-1]:
                a = Bin_num(binary = [self.binvalue[i]])
                b = Bin_num(binary = [bin.binvalue[i]])
                (s, carry) = a.onebit_adder(b, carry)
        
                ans.insert(0, s.binvalue[0])
            ansbin = Bin_num(binary = ans)

            return ansbin, carry

    def nbit_adder2s(self,bin):
        '''detects overflow for 2s complement addition NOT CURRENTLY WORKING'''
        (s, carry) = self.nbit_adder(bin)
        
        a = Bin_num(binary = [self.binvalue[0]])
        b = Bin_num(binary = [bin.binvalue[0]])

        ab = a.logicxor(b)
        ab = ab.logicnot()

        print a.binvalue, b.binvalue
        print ab.binvalue, carry.binvalue
        overflow = carry.logicxor(ab)

        return (s, overflow)