import base64
from pwn import *
encoded="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
par_flag="crypto{"
key='myXORkey'
print(f"flag: {xor(key,bytes.fromhex(encoded).decode('utf-8'))}")

#flag: b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
