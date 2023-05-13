from Crypto.Util.number import long_to_bytes
'''pip install pycryptodome'''
# from factordb get the value of p and q
p = 752708788837165590355094155871
q = 986369682585281993933185289261
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
tot = (p - 1) * (q - 1)
d = pow(e, -1, tot)
print(f"private key: {d}")
ct = 39207274348578481322317340648475596807303160111338236677373
pt = pow(ct, d, n)
pt = long_to_bytes(pt)
print(pt)

#flag - crypto{N33d_b1g_pR1m35}