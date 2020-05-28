import sys
import time

def ft_progress(lst):
	# eta = current elapsed time / current cycle number * max cycle number - current elapsed time
	start = time.perf_counter()
	for i in lst:
		if i == 0:
			eta = 0
		else:
			eta = (time.perf_counter() - start) / i * len(lst) - (time.perf_counter() - start)
		elapsed = time.perf_counter() - start
		percent = (i+1)/len(lst)*100
		bar = ''
		bar = bar.rjust(int(i/len(lst)*20), '=')
		bar += '>'
		bar = bar.ljust(20, ' ')
		erase_line = '\x1b[2K'
		if i+1 == len(lst):
			print(erase_line + "ETA: %.2fs [%3.0f%%][%s] %i/%i | elapsed time %.2fs" % (eta, percent, bar, i + 1, len(lst), elapsed))
		else:
			print(erase_line + "ETA: %.2fs [%3.0f%%][%s] %i/%i | elapsed time %.2fs" % (eta, percent, bar, i + 1, len(lst), elapsed), end="\r", flush=True)
		yield i
