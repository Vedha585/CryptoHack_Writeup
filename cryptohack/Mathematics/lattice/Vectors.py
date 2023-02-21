u=[7,7,2] #3*(2*v - w) ∙ 2*u
v=[2,6,3]
w=[1,0,0]

v=[2*i for i in v]
X=[3*(i-j) for (i,j) in zip(v,w)]
u=[2*i for i in u]
res=0
for ele1,ele2 in zip(X,u):
  res+=ele1*ele2

print(res)