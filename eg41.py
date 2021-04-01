class TMRange:
  def __init__(k,end,start=1,step=1):
    k.start=start
    k.current=k.start
    k.end=end
    k.step=step


  def __str__(k):
    return f"TMRange({k.start},{k.end})"

  def __iter__(k):
    return k

  def __next__(k):
    if k.current>k.end: raise StopIteration("Iteration end")
    data=k.current
    k.current=k.current+k.step
    return data


myrange=TMRange(5)
print(myrange)

for u in myrange:
  print(u)

j=TMRange(50,60,3)

for u in j:
  print(u)