from pwn import * # pip install pwntools
import json
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decoding(to_decode,encoded):
        if to_decode=="base64":
                return base64.b64decode(encoded).decode('utf-8')
        elif to_decode == "hex":
                return bytes.fromhex(encoded).decode('utf-8')
        elif to_decode == "rot13":
                return codecs.decode(encoded,'rot_13')
        elif to_decode == "bigint":
                encoded=bytes.fromhex(encoded[2:]).decode('utf-8')
                return encoded
        elif to_decode == "utf-8":
                return ("".join(chr(b) for b in encoded))

for i in range(101):
    received = json_recv()
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    decoded=decoding(received["type"],received["encoded"])
    print(f"decoded value: {decoded}")
    to_send = {    "decoded": f'{decoded}'}
    print(to_send)
    json_send(to_send)
    #json_recv()
