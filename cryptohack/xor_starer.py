from pwn import *

enc_str="label"

lst1=[]

for e in enc_str:
	lst1.append(ord(e)^13)

print("".join(chr(o) for o in lst1))

