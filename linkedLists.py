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
  self.tail = root

 def __insert_head(self, node):
  node = SLNode(node)
  node.set_next(self.root)
  self.root = node
  if not self.tail: self.tail = self.root

 def __insert_tail(self, node):
  node = SLNode(node)
  node.set_next(None)
  self.tail.set_next(node)

 def insert(self, node, type='head'):
  {
   'head' : self.__insert_head,
   'tail' : self.__insert_tail
  }[type](node)
  

 def get_last(self):
  node = self.root
  
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
 


   

 
   
  
   
