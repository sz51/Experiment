import os
import multiprocessing
import time

def bar(i, m, j):
	parser = './ltlf2ws1s '
	path = '../../../Benchmark/Scalability/benchmark/case_'
	filename = path+str(i)+'_'+str(m)+'_50/'+str(j)+'.ltlf'
	tmp = ' >tmp_dfa.mona'
	exe = './mona -w -q tmp_dfa.mona '
	directory = "../output_mona/case_"+str(i)+"_"+str(m)+"_50"
	if not os.path.exists(directory):
		os.makedirs(directory)
	outfile = '../output_mona/case_'+str(i)+'_'+str(m)+'_50/'+str(j)+'.out'
	from time import clock
	start = clock()
	os.system(parser + filename + tmp)
	os.system(exe + '> mona_out')
	finish = clock()
	f = open(outfile, "a")         
	print >> f, "Total time is: %f" % ((finish-start))
	f.close()


i = 1
while i <= 10:
	m = 100
	while m <= 500:
		j = 1
		while j <= 50:
			p = multiprocessing.Process(target=bar, args = (i, m, j))
			p.start()
			p.join(60)
			if p.is_alive():
				outfile = '../output_mona/case_'+str(i)+'_'+str(m)+'_50/'+str(j)+'.out'
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



