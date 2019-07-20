import time, sys

for i in range(200):
	percent = i/200.0;
	hashes = "#" * int(percent * 20)
	spaces = " " * (20 - len(hashes))
	sys.stdout.write("\r" + "[" + hashes + spaces + "]")
	sys.stdout.flush()
	time.sleep(0.2)