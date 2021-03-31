def lmn(x):
  print(x)
  def pqr():
    print(x)
    print("Cool concept")
  return pqr


j=lmn(300)
j()
m=lmn(400)
m()
j()