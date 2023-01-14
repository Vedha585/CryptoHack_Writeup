from Crypto.Util.number import *

string="HELLO"

lst=[]
for e in string:
	lst.append(ord(e))
print(lst)

for i in range(len(lst)):
	lst[i]=hex(lst[i])[2:]

print("0x"+"".join(lst))
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
