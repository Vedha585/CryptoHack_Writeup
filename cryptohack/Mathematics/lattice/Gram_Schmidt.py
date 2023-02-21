def prod_vec(v1,v2):
  res=0
  for ele1,ele2 in zip(v1,v2):
    res+=ele1*ele2
  return res

def add_vec(vector):
  res_vec=[0,0,0,0]
  for ele in vector:
    res_vec=np.array(res_vec)+np.array(ele)
  return res_vec

def two_vec_add(v1,v2):
  v=[]
  for ele1,ele2 in zip(v1,v2):
    v.append(ele1+ele2)
  return v

def scal_mul(v,k):
  v=[k*i for i in v ]
  return v

def Gram_Schmidt(basis):
  orth_basis=[]
  orth_basis.append(basis[0])
  for i in range(1,len(basis)):
    vec=[]
    for j in range(len(orth_basis)):
      sca=prod_vec(basis[i],orth_basis[j])/prod_vec(orth_basis[j],orth_basis[j])
      vec.append(scal_mul(orth_basis[j],sca))
    res_add=scal_mul(add_vec(vec),-1)
    orth_basis.append(two_vec_add(res_add,basis[i]))
  return orth_basis


basis=[[4,1,3,-1],[2,1,-3,4],[1,0,-2,7],[6, 2, 9, -5]]
orth_basis=Gram_Schmidt(basis)
print(round(orth_basis[3][1],5))
