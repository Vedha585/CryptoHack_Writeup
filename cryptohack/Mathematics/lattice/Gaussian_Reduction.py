import math
import numpy as np
def vec_len(v1,v2):
  res=0
  for ele1,ele2 in zip(v1,v2):
    res+=ele1*ele2
  return res

def gauss_red(v1,v2):
  while True:
    if vec_len(v2,v2) < vec_len(v1,v1):
      v1,v2=v2,v1
    m=math.floor(vec_len(v1,v2)/vec_len(v1,v1))
    print(m)
    if m==0:
      return (v1,v2)
    else:
      v2=np.array(v2)+np.array(np.dot(m*-1,v1))
  return


v=[846835985, 9834798552]
u=[87502093, 123094980]
b1,b2=gauss_red(v,u)
print(f"basis 1: {b1} , basis 2:{b2} ")
print(f"inner product of the two basis : {vec_len(b1,b2)}")