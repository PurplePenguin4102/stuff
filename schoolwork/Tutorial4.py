def is_dna(string):
    
    if len(string) % 3 == 0:
        i = 0
        for c in string:
            if c in "ATGC":
                i += 1
        if i == len(string):
            return True
        else:
            return False
    else:
        return False

def reverse_complement(string):

    rules = {"A": "T",
             "T": "A",
             "C": "G",
             "G": "C"}
    ans = ''
    if is_dna(string):
        for c in string:
            ans += rules[c]
        return ans[::-1]

def print_codons(string):

    if is_dna(string):
        i = 0
        while i <= len(string):
            print string[i:i+3]
            i += 3

def get_number(string):

    ans = ''
    for c in string + " ":
        if c.isdigit():
            ans += c
        else:
            if len(ans) > 0:
                return int(ans)

def get_number2(string):

    ans = ''

    for i,c in enumerate(string + " "):
        if (c == '-') and (len(ans) == 0):
            if string[i+1].isdigit():
                ans += c
        elif c.isdigit():
            ans += c
        else:
            if len(ans) > 0:
                return int(ans)
