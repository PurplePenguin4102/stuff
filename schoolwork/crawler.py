import urllib2
import time
import random
# help(urllib2)


def get_html(startname):
	startname = startname.split(" ")
	insertname = ""
	for name in startname:
		insertname += name + '+'

	time.sleep(random.randint(2,10))
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	try:
		f = opener.open('http://www.music-map.com/' + insertname[:-1] + '.html')
		html = f.read()
	except Exception:
		return None
		

	return html.splitlines()

def get_namelist(lines):

	test = '<a href'
	artists = [s for s in lines if s[:7] == test]

	namelist = []
	for html in artists:
	
		f = html.find('id=')
		name = html[f+6:-4]
		if name.startswith('>'):
			name = name[1:]

		namelist.append(name)

	return namelist

def make_node(inputname):

	lines = get_html(inputname)
	if lines == None:
		return None
	namelist = get_namelist(lines)
	
	return (inputname, namelist)

def zero_step(name):

	masternode = make_node(name)
	masterlist.append(masternode)

	return masterlist

def one_step(namelist, masterlist):

	for i in xrange(len(namelist)):
		testednames = [node[0] for node in masterlist]	
		print len(namelist)
		print len(masterlist)
		
		if namelist[i] in testednames: pass
		else: 
			print i, namelist[i]
			node = make_node(namelist[i])
		
		if node:

			masterlist.append(node)
			datastr = make_data(masterlist)
			f = open('twostep.txt','w')
			f.write(str(datastr))
			f.close()

		print node
		 

	return masterlist

def make_data(masterlist):

	datastr = ""
	for node in masterlist:
		datastr += node[0] + ','
		for name in node[1]:
			datastr += name + ','
		datastr += "\n"

	return datastr

def make_masterlist_from_file(filename):

	f = open(filename, 'rU')
	data = f.read()
	data = data.strip()
	data = data[3:]
	data = data.splitlines()

	masterlist = []
	for line in data:
		line = line.split(',')
		line.pop()
		
		namelist = line[1:]
		name = line[0]
		node = (name,namelist)
		masterlist.append(node)

	return masterlist

def main():

	# masterlist = zero_step("Justin Bieber")
	# datastr = make_data(masterlist)

	# f = open('zerostep.txt', 'w')
	# f.write(datastr)
	# f.close()

	# namelist = [name for name in masterlist[0][1]]

	# print namelist
	# masterlist = one_step(namelist)
	# datastr = make_data(masterlist)
	
	# f = open('onestep.txt', 'w')
	# f.write(str(datastr))
	# f.close()

	masterlist2 = make_masterlist_from_file('twostep.txt')
	masterlist1 = make_masterlist_from_file('onestep.txt')

	namelist = list(set([name for node in masterlist1 for name in node[1]]) - set([node[0] for node in masterlist1]))
 	
 	namelist.remove(' Wind And Fire')
 	namelist.remove('Earth')

 	testedlist = [node[0] for node in masterlist2]
 	for name in testedlist:
		if name in namelist: namelist.remove(name)

	masterlist = one_step(namelist, masterlist2)

if __name__ == '__main__':
	masterlist = []
	masternodelist = []
	main()