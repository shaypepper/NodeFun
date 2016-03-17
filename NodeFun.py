print " My tree:" 
print "            A"
print "           /|\\"
print "          B C D"
print "         /|   |\\"
print "        E F   G H"
print "       /|     |\\"
print "      I J     K L"

class Node(object):
  def __init__(self, key, value):
    self.value = value
    self.children = []
    self.key = key
  
  def addChildren(self, children, locale = -1):
    if locale < 0:
      locale = len(self.children)
    x = 0
    for child in children: 
      self.children.insert(locale + x, child)
      x += 1
    # print self.key, self.children
      
  def addChild(self, child, locale = -1):
    if locale < 0:
      locale = len(self.children)
    self.children.insert(locale, child)
    # print self.key, self.children
    
  def getChildren(self):
    return self.children
    
  def hasChildren(self):
    return (self.getChildren != [])
  
  def setValue(self, value):
    self.value =  value
    
  def getValue(self):
    return self.value
    
  def setKey(self, key):
    self.key =  key
    
  def getKey(self):
    return self.key
    
  def removeChildWithKey(self, key): 
    for child in self.children:
      if child.key == key:
        return self.children.pop(child)
        
  def removeChildWithVar(self, child): 
    self.children.remove(child)
    
  def checkValue(self, value):
    # print "[%s, %s]" % (self.key, self.value)
    if value == self.value:
      return True
    else: 
      return False
      
  def checkKey(self, key):
    print "[%s, %s]" % (self.key, self.value)
    if key == self.key:
      return True
    else: 
      return False

A = Node('A', 1)
B = Node('B', 2)
C = Node('C', 3)
D = Node('D', 4)
E = Node('E', 5)
F = Node('F', 6)
G = Node('G', 7)
H = Node('H', 8)
I = Node('I', 9)
J = Node('J', 10)
K = Node('K', 11)
L = Node('L', 12)


A.addChildren([B, C, D])
B.addChildren([E, F])
C.addChildren([])
D.addChildren([G, H])
E.addChildren([I, J])
F.addChildren([])
G.addChildren([K, L])
H.addChildren([])
I.addChildren([])
J.addChildren([])
K.addChildren([])
L.addChildren([])


def traversePostOrder(root, value):
  if root.hasChildren():
    for child in root.getChildren():
      x = traversePostOrder(child, value)
      if x != None:
        return x 
  if root.checkValue(value):
    print "***{%s}***" %(root.key)
    return root
  else:
    print "%s ->" % (root.key),

    
def traversePreOrder(root, value):
  if root.checkValue(value): 
    print "***{%s}***" %(root.key)
    return root
  else: 
    print "%s ->" % (root.key),
    if root.hasChildren():
      for child in root.getChildren():
        x = traversePreOrder(child, value)
        if x != None:
          return x 

traversePostOrder(A,1)
traversePreOrder(A,8)
     