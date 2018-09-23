class SLNode(object):

 def __init__(self, data=None, next_node=None):
  self.data = data
  self.next_node = next_node

 def get_data(self):
  return self.data

 def get_next(self):
  return self.next_node

 def set_next(self, next_node):
  self.next_node = next_node

 def make_tail(tail_node=None):
  self.next_node = tail_node

class DLNode(object):

 def __init__(self, data=None, prev_node=None, next_node=None):
  self.data = data
  self.next_node = next_node
  self.prev_node = prev_node

 def get_data(self):
  return self.data

 def get_next(self):
  return self.next_node

 def get_prev(self):
  return self.prev_node

 def set_next(self, next_node):
  self.next_node = next_node

 def set_prev(self, prev_node):
  self.prev_node = prev_node

 def make_tail(tail_node=None):
  self.next_node = tail_node

 def make_root(root_node=None):
  self.prev_node = root_node

class SLList(object):

 def __init__(self, root=None):
  self.root = root
  self.current = root
  self.tail = root

 def __insert_head(self, node):
  if not isinstance(node, SLNode):
   node = SLNode(node)
  node.set_next(self.root)
  self.root = node
  if not self.tail: self.tail = self.root

 def __insert_tail(self, node):
  if not isinstance(node, SLNode):
   node = SLNode(node)
  if self.tail: 
   self.tail.set_next(node)
   while True:
    next_node  = self.tail.get_next()
    if not next_node: break
    self.tail = next_node
  else: self.__insert_head(node)
    
 def insert(self, node, type='head'):
  {
   'head' : self.__insert_head,
   'tail' : self.__insert_tail
  }[type](node)
  

 def get_last(self):
  return self.tail
  
 def size(self):
  count, current = 0, self.root
  while current:
   count +=1
   current = current.get_next()
  return count

 def search(self, item):
  current =  self.root
  while current:
   if current.get_data()==item: return True
   current = current.get_next()
  return False

 def delete(self, item):
  prev, current = None, self.root
  while current:
   if current.get_data() == item:
    if prev: prev.set_next(current.get_next())
    else: self.root = current.get_next()
    return True
   prev, current = current, current.get_next()
  return False

 def get_all(self):
  current = self.root
  while current:
   yield current.get_data()
   current = current.get_next()

 def print_all(self):
  print(list(self.get_all()))

 def get_data(self):
  return self.current.get_data()

 def get_next(self):
  prev = self.current
  if prev: self.current = self.current.get_next()
  return prev 

 def get(self):
  return self.current
  

 def reset(self):
  self.current = self.root

def merge_sorted_SLList(L1, L2):
 temp = SLList()
 while L1.get() and L2.get():
  if L1.get_data() > L2.get_data():
   temp.insert(L1.get_data(), 'tail')
   L1.get_next()
  else:
   temp.insert(L2.get_data(), 'tail')
   L2.get_next()

 temp.insert(L1.get_next() or L2.get_next(), 'tail')
 return temp
 

if __name__ == '__main__':
 temp = SLList()
 temp.insert(1)
 temp.insert(2)
 temp.insert(3)
 print(temp.size())
 temp.print_all()
 temp.insert(4)
 temp.print_all()
 temp.delete(2)
 temp.print_all()
 temp.insert(7, 'tail')
 temp.print_all()
 print (temp.size())
 
 L1 = SLList()
 L2 = SLList()
 
 L1.insert(7)
 L1.insert(5)
 L1.insert(2)
 L1.print_all()

 L2.insert(11)
 L2.insert(3)
 L2.print_all()

 L = merge_sorted_SLList(L1, L2)
 L.print_all()

   

 
   
  
   
