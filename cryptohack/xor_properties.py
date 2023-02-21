import base64
from pwn import *
key1="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key_1_or_2="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2=xor(bytes.fromhex(key1),bytes.fromhex(key_1_or_2))
#print(base64.b64encode(bytes.fromhex(key1)))
print(f"key2: {key2.hex()}")
key_2_or_3="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key3=xor(bytes.fromhex(key_2_or_3),key2)
print(f"key3: {key3.hex()}")
flag_1_2_3="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag=xor(bytes.fromhex(flag_1_2_3),bytes.fromhex(key1),key2,key3)
print(f"flag : {flag.decode('utf-8')}")

#flag : crypto{x0r_i5_ass0c1at1v3}
