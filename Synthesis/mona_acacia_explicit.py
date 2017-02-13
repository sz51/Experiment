import os
import multiprocessing
import time

def bar(i, j):
	parser = './ltlf2ws1s '
	filename = '../acacia/'+str(i)+'.ltlf'
	partfile = '../acacia/'+str(i)+'.part'
	tmp = ' >tmp.mona'
	exe = './mona -w -q tmp.mona >tmp.out'
	syn = './bdd2 tmp.dfa '
	directory = "../mona_acacia_explicit/"
	if not os.path.exists(directory):
		os.makedirs(directory)
	outfile = '../mona_acacia_explicit/'+str(i)+'.out'
	from time import clock
	start = clock()
	os.system(parser + filename + tmp)
	os.system(exe)
	f = open(outfile, "a")  
	DFAfinish = clock()
	print >> f, "DFA time is: %f" % ((DFAfinish-start))
	os.system(syn + partfile + ' >' + outfile )
	Totalfinish = clock()
	print >> f, "Syn time is: %f" % ((Totalfinish-DFAfinish))
	print >> f, "Total time is: %f" % ((Totalfinish-start))
	f.close()


i = 0
j = 0
while i <= 79:
	p = multiprocessing.Process(target=bar, args = (i,j))
	p.start()
	p.join(180)
	if p.is_alive():
		outfile = '../mona_acacia_explicit/'+str(i)+'.out'
		# os.system('rm '+ outfile)
		f = open(outfile, "a")         
		print >> f, "KILL"
		print outfile
		print "KILL"
		f.close()
		p.terminate()
		p.join()
	i = i + 1



