import base64

enc_flag="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

print(bytes.fromhex(enc_flag))
enc_flag=base64.b64encode(bytes.fromhex(enc_flag))
print(enc_flag)
#print(base64.b64decode(enc_flag))
