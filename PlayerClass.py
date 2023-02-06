class Player:
  lantern = False
  rope = False
  knife = False
  planks = False
  door = False
  bottle = False
  rations = False
  medallion = False
  survived = False

  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

  def hasRaftMaterials(self):
    if(self.rope and self.knife and self.planks and self.door):
      return True
    else:
      return False
    