#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

py_time = []
cpp_time = []

def main():
	I = Integer(0)
	nlst = range(0,45)
	for i in nlst:
		I.set(i)

		start = pc()
		print(I.fib())
		end = pc()
		cpp_time.append(end - start)

		start = pc()
		print(fib_py(i))
		end = pc()
		py_time.append(end - start) 

	I.set(47)
	start = pc()
	print("Test 47 cpp: ", I.fib())
	end = pc()
	print("Time for n = 47 with cpp: ", end - start) 
	
	plt.plot(nlst, cpp_time, 'b.', nlst, py_time, 'r.')
	plt.xlabel('Iterations (n)')
	plt.ylabel("Time for fibonacci (s)")
	plt.savefig('fib_py_cpp.png')
	
		
		



def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n-1) + fib_py(n-2)

if __name__ == '__main__':
	main()


