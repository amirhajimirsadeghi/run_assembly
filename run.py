import sys
R = [	
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
	]
M = [
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
	]

register = { '$acc':0, '$r1': 1, '$r2': 2, '$r3': 3, '$r4': 4, '$r5': 5, '$r6': 6, '$r7': 7, '$r8': 8 }
OVERFLOW = 0
BRANCH_SET = 0
BRANCH_IMM = [0,0,0,0,0,0,0,0]

def bin_to_int(arr):
	if len(arr) != 8:
		raise ValueError('you tried to turn array of size > 8 into number')
	i = 0
	total = 0
	for x in arr[::-1]:
		total = total + (pow(2,i)*x)
		i = i+1
	return total

def int_to_bin(num):
	if num > 255 or num < 0:
		raise ValueError('you tried to turn number bigger than 8 bits into binary')
	retVal = [0,0,0,0,0,0,0,0]
	i = 7
	while num != 0:
		retVal[i] = num%2
		num = num/2
		i = i-1
	return retVal

def abs(arr_og):
	arr = arr_og[:]
	value = bin_to_int(arr)
	if value >= 128:
		idx = 0
		while idx < 8:
			arr[idx] = arr[idx]^1
			idx = idx+1
		value = bin_to_int(arr)+1
		return(int_to_bin(value))
	else:
		return arr
def sr(arr):
	working = [0,0,0,0,0,0,0,0]
	i = 6
	while i >= 0:
		working[i+1] = arr[i]
		i = i-1
	return working

def sl(arr):
	working = [0,0,0,0,0,0,0,0]
	i = 1
	while i < 8:
		working[i-1] = arr[i]
		i = i+1
	return working

def run_machine_code(lines):
	return 0

def run_assembly(lines):
	global BRANCH_SET
	global BRANCH_IMM
	global OVERFLOW
	global R
	global M
	global register
	i = 0
	while i < len(lines):
		y = lines[i].split()
		print i,
		print ": ",
		print y

		if y[0].lower() == "add":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(R[0]) + bin_to_int(reg)
			if value > 255:
				OVERFLOW = 1
				value = value-256
			R[0] = int_to_bin(value)

		elif y[0].lower() == "sub":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(R[0]) - bin_to_int(reg)
			R[0] = int_to_bin(value)

		elif y[0].lower() == "inc":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(reg)+1
			if value > 255:
				OVERFLOW = 1
				value = 0
			R[register[y[1].lower()]] = int_to_bin(value)

		elif y[0].lower() == "aof":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(reg) + OVERFLOW
			OVERFLOW = 0
			R[register[y[1].lower()]] = int_to_bin(value)

		elif y[0].lower() == "clr":
			R[register[y[1].lower()]] = [0,0,0,0,0,0,0,0]

		elif y[0].lower() == "abs":
			reg = R[register[y[1].lower()]]
			R[register[y[1].lower()]] = abs(reg)

		elif y[0].lower() == "sl":
			reg = R[register[y[1].lower()]]
			R[register[y[1].lower()]] = sl(reg)

		elif y[0].lower() == "sr":
			reg = R[register[y[1].lower()]]
			R[register[y[1].lower()]] = sr(reg)

		elif y[0].lower() == "ator":
			reg = R[register[y[1].lower()]]
			R[register[y[1].lower()]] = R[0]

		elif y[0].lower() == "rtoa":
			reg = R[register[y[1].lower()]]
			R[0] = reg

		elif y[0].lower() == "corr":
			reg = R[register[y[1].lower()]]
			#TODO

		elif y[0].lower() == "ld":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(reg)
			R[0] = M[value]

		elif y[0].lower() == "st":
			reg = R[register[y[1].lower()]]
			value = bin_to_int(reg)
			M[value] = R[0]
			
		elif y[0].lower() == "seql":
			reg = R[register[y[1].lower()]]
			value_r = bin_to_int(reg) & 15
			value_a = bin_to_int(R[0]) & 15
			if value_r == value_a:
				BRANCH_SET = 1

		elif y[0].lower() == "seq":
			reg = R[register[y[1].lower()]]
			value_r = bin_to_int(reg)
			value_a = bin_to_int(R[0])
			if value_a == value_r:
				BRANCH_SET = 1

		elif y[0].lower() == "slt":
			reg = R[register[y[1].lower()]]
			value_r = bin_to_int(reg)
			value_a = bin_to_int(R[0])
			if value_a < value_r:
				BRANCH_SET = 1

		elif y[0].lower() == "sgt":
			reg = R[register[y[1].lower()]]
			reg = R[register[y[1].lower()]]
			value_r = bin_to_int(reg)
			value_a = bin_to_int(R[0])
			if value_a > value_r:
				BRANCH_SET = 1

		elif y[0].lower() == "se":
			reg = R[register[y[1].lower()]]
			if reg[7] == 0:
				BRANCH_SET = 1

		elif y[0].lower() == "xor":
			reg = R[register[y[1].lower()]]
			acc = R[0]
			working = [0,0,0,0,0,0,0,0]
			xor_i = 0
			while xor_i < 8:
				working[xor_i] = reg[xor_i] ^ acc[xor_i]
				xor_i = xor_i+1
			R[0] = working

		elif y[0].lower() == "clrb":
			BRANCH_IMM = [0,0,0,0,0,0,0,0]

		elif y[0].lower() == "seth":
			value_hi = int(y[1])*16
			value_lo = bin_to_int(R[0]) & 15
			R[0] = int_to_bin(value_hi+value_lo)

		elif y[0].lower() == "setl":
			value = int(y[1])
			R[0] = int_to_bin(value)

		elif y[0].lower() == "sbh":
			value_hi = int(y[1])*16
			value_lo = bin_to_int(BRANCH_IMM) & 15
			BRANCH_IMM = int_to_bin(value_lo + value_hi)

		elif y[0].lower() == "sbl":
			value = int(y[1])
			BRANCH_IMM = int_to_bin(value)

		elif y[0].lower() == "bs":
			value = int(y[1])
			if BRANCH_SET == 1:
				i = i + value
				BRANCH_SET = 0
				print ""
				continue

		elif y[0].lower() == "bns":
			value = int(y[1])
			if BRANCH_SET == 0:
				i = i + value
				print ""
				continue
			BRANCH_SET = 0

		elif y[0].lower() == "print":
			print "M: ",
			print M
			print "R: ",
			print R
		
		else:
			print "unrecognized command" + y[0] + " on line " + str(i)
			return;
		i = i + 1
	print "M : ",
	print M
	print "R: ",
	print R

if __name__ == "__main__":
	'''
		MANIPULATE MEMORY HERE BEFORE EXECUTING
		YOUR ASSEMBLY
	'''
	#open file
	if(len(sys.argv) >= 2):
		lines = []
		lines2 = []
		with open(sys.argv[1]) as f:
			lines = f.readlines()
			for x in lines:
				lines2.append(x.strip())
			lines = []
			for x in lines2:
				if x:
					lines.append(x)
		while True:
			var = raw_input("Is this machine code? (y/n): ")
			if var[0] == 'y':
				run_machine_code(lines)
				break;
			elif var[0] == 'n':
				run_assembly(lines)
				break;
	else:
		print "please specify filename when executing"
	print R[5],
	print R[4]