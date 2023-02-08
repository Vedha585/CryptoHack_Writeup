p, q = 32321, 26513
def Extended_Gcd(a, b):
  if a == 0:
    return b, 0, 1
  else:
    gcd, x, y = Extended_Gcd(b % a, a)
    return gcd, y - (b // a) * x, x


if __name__ == "__main__":
  gcd,x,y=Extended_Gcd(p, q)
  print(f"gcd: {gcd} = {p}x{x}+{q}+{y}")


