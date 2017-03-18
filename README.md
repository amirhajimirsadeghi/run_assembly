Usage:
	python run.py <filename>

File format:
	- format registers $acc, $r1-$r7
	- remove all comments that exist on their own line
	- have all jumps be literal
	- pass all immediates as integers

Assuming:
	- sub works as: acc = acc - reg
	- shifting doesn't use overflows
	- assuming xor works: acc = acc ^ reg
	- setl clears top 4 bits, seth clears nothing
	- Input is from M[1] - M[4]
	- after calling bs or bns branch bit is reset to 0
TODO:
	- how do we act if subtract leads to negative?/ will it ever?
	- how do we handle abs(-128)?



Might need later:

'''
opcode = {	
	'000001': add(curr_reg),'000010': sub(curr_reg),'000011': inc(curr_reg),'000100': aof(curr_reg),
	'000101': clr(curr_reg),'000110': abs(curr_reg), '000111': sl(curr_reg),'001000': sr(curr_reg),
	'001001': ator(curr_reg),'001010': rtoa(curr_reg),'001011': corr(curr_reg),'001100': ld(curr_reg),
	'001101': st(curr_reg),'001110': seql(curr_reg),'001111': seq(curr_reg),'010000': slt(curr_reg),
	'010001': sgt(curr_reg),'010010': se(curr_reg),'010011': xor(curr_reg),'010100': clrb(),
	'01100': seth(immediate),'01101': setl(immediate),'01110': sbh(immediate),'01111': sbl(immediate),
	'10': bs(immediate),'11': bns(immediate)
}

options = {
	'Add': add(curr_reg),'Sub': sub(curr_reg),'Inc': inc(curr_reg),'Aof': aof(curr_reg),
	'Clr': clr(curr_reg),'abs': abs(curr_reg),'Sl': sl(curr_reg),'Sr': sr(curr_reg),
	'ator': ator(curr_reg),'rtoa': rtoa(curr_reg),'corr': corr(curr_reg),'Ld': ld(curr_reg),
	'St': st(curr_reg),'seql': seql(curr_reg),'seq': seq(curr_reg),'slt': slt(curr_reg),
	'sgt': sgt(curr_reg),'se': se(curr_reg),'xor': xor(curr_reg),'clrb': clrb(),
	'seth': seth(immediate),'setl': setl(immediate),'sbh': sbh(immediate),
	'sbl': sbl(immediate),'bs': bs(immediate),'bns': bns(immediate)
}
'''