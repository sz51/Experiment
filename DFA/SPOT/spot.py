import os
import multiprocessing
import time

def bar(i, m, j):
	parser = '../../spot-2.2.2/bin/ltlfilt --from-ltlf -F '
	filename = '../benchmarks/case_'+str(i)+'_'+str(m)+'_50/'+str(j)+'.ltlf'
	exe = ' | ltl2tgba -D'
	directory = "../output_spot/case_"+str(i)+"_"+str(m)+"_50"
	if not os.path.exists(directory):
		os.makedirs(directory)
	outfile = '../output_spot/case_'+str(i)+'_'+str(m)+'_50/'+str(j)+'.out'
	from time import clock
	start = clock()
	os.system(parser + filename + exe + '> spot_out')
	finish = clock()
	f = open(outfile, "a")         
	print >> f, "Total time: %f" % ((finish-start))
	f.close()

i = 1
while i <= 10:
	m = 100
	while m<= 500:
		j = 1
		while j <= 50:
			p = multiprocessing.Process(target=bar, args = (i, m, j))
			p.start()
			p.join(60)
			if p.is_alive():
				outfile = '../output_spot/case_'+str(i)+'_'+str(m)+'_50/'+str(j)+'.out'
				# os.system('rm '+ outfile)
				f = open(outfile, "w")         
				print >> f, "KILL"
				print outfile
				print "KILL"
				f.close()
				p.terminate()
				p.join()
			j = j + 1
		m = m + 50
	i = i + 1



