import base64
from pwn import *
encoded="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
key_par0=bytes.fromhex(encoded).decode('utf-8')[:7:1]
par_flag="crypto{"
key_par=xor(key_par0,par_flag)
print(xor(key_par,bytes.fromhex(encoded)).decode('utf-8'))

#flag : crypto{0x10_15_my_f4v0ur173_by7e}
