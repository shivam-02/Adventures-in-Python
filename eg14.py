class PartyAnimal:
  x=0
  def __init__(self):
    print("I am constructed")

  def party(self):
    self.x=self.x+1
    print(self.x)

  def __del__(self):
    print("I am destructed")


x=PartyAnimal()
x.party()
