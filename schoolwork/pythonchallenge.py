a = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

keydict = {'a':1,
		   'b':2,
		   'c':3,
		   'd':4,
		   'e':5,
		   'f':6,
		   'g':7,
		   'h':8,
		   'i':9,
		   'j':10,
		   'k':11,
		   'l':12,
		   'm':13,
		   'n':14,
		   'o':15,
		   'p':16,
		   'q':17,
		   'r':18,
		   's':19,
		   't':20,
		   'u':21,
		   'v':22,
		   'w':23,
		   'x':24,
		   'y':25,
		   'z':26}
lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
url = "http://www.pythonchallenge.com/pc/def/map.html"
b = ''
for c in url:
	if c in " '().:/":
		b += c
	else:
		b += lst[(keydict[c]+1)%26]
print b