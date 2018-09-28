class SLList(object):
 def __init__(self, data='root', next=None):
  self.data = data
  self.next = next  

 @staticmethod
 def search_list(L, key):
  while L and L.data != key : L = L.next
  return L

 @classmethod
 def insert_after(cls, node, new_node):
  if not isinstance(new_node, cls): new_node = cls(new_node) 
  new_node.next = node.next
  node.next = new_node

 @staticmethod
 def delete_after(node):
  node.next = node.next.next

 @staticmethod
 def get_list(L):
  if L.data == 'root': L=L.next
  while L: 
   yield L.data
   L = L.next

 @classmethod
 def count(cls, L):
  L = cls.skip_root(L)
  count = 0
  while L:
   count+=1
  L = L.next
  return count

 @classmethod
 def print_all(cls, L):
  print(list(cls.get_list(L)))

 @staticmethod
 def skip_root(L):
  return L.next if L.data == 'root' else L

 @classmethod
 def merge_sorted_list(cls, L1, L2):
  dummy_head = tail = cls()
  L1 = cls.skip_root(L1)
  L2 = cls.skip_root(L2)
 #print_all(L1)
 #print_all(L2)
  while L1 and L2:
  #print_all(L1)
  #print_all(L2)
   if L1.data > L2.data:
    tail.next, L1 = L1, L1.next
   else:
    tail.next, L2 = L2, L2.next
   tail = tail.next
  #print_all(tail) 
  tail.next = L1 or L2 
  return cls.skip_root(dummy_head)


temp = SLList()
SLList.insert_after(temp, 6)
SLList.insert_after(temp, 7)
SLList.insert_after(temp, 8)

SLList.print_all(temp)

print(SLList.count(temp))

L1 = SLList()
SLList.insert_after(L1, 2)
SLList.insert_after(L1, 5)
SLList.insert_after(L1, 7)

SLList.print_all(L1)

L2 = SLList()
SLList.insert_after(L2, 3)
SLList.insert_after(L2, 11)
SLList.print_all(L2)


L = SLList.merge_sorted_list(L1, L2)
SLList.print_all(L)
