Usage:
	`python run.py <filename>`

File format:
	- format registers $acc, $r1-$r7
	- remove all comments that exist on their own line
	- have all jumps be literal
	- pass all immediates as integers

Assumptions:
	- sub works as: acc = acc - reg
	- shifting doesn't use overflows
	- assuming xor works: acc = acc ^ reg
	- setl clears top 4 bits, seth clears nothing
	- Input is from M[1] - M[4]
	- after calling bs or bns branch bit is reset to 0

TODO:
	- how do we act if subtract leads to negative?/ will it ever?
	- how do we handle abs(-128)?
