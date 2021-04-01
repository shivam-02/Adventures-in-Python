class TMRange:
  def __init__(self,start,end,step=1):
     self.start=start
     self.end=end
     self.step=step
     if self.step==0: raise ValueError("Step is zero")

  def __iter__(self):
     return TMRangeIterator(self)

  def __str__(self):
     return f"TMRange({self.start},{self.end})"


class TMRangeIterator:
  def __init__(self,obj):
    self.start=obj.start
    self.end=obj.end
    self.step=obj.step
    self.current=self.start

  def __next__(self):
     if self.current>self.end: raise StopIteration
     self.data=self.current
     self.current=self.current+self.step
     return self.data

  def __str__(self):
      return f"TMRangeIterator({self.start},{self.end})"
      

