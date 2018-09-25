class SLList(object):
 def __init__(self, data='root', next=None):
  self.data = data
  self.next = next

def search_list(L, key):
 while L and L.data != key : L = L.next
 return L

def insert_after(node, new_node):
 if not isinstance(new_node, SLList): new_node = SLList(new_node) 
 new_node.next = node.next
 node.next = new_node

def delete_after(node):
 node.next = node.next.next

def get_list(L):
 if L.data == 'root': L=L.next
 while L: 
  yield L.data
  L = L.next

def count(L):
 if L.data == 'root': L=L.next
 count = 0
 while L:
  count+=1
  L = L.next
 return count

def print_all(L):
 print(list(get_list(L)))

skip_root = lambda L: L.next if L.data == 'root' else L

def merge_sorted_list(L1, L2):
 dummy_head = tail = SLList()
 L1 = skip_root(L1)
 L2 = skip_root(L2)
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
 print_all(tail) 
 tail.next = L1 or L2
 
 return skip_root(dummy_head)


temp = SLList()
insert_after(temp, 6)
insert_after(temp, 7)
insert_after(temp, 8)

print_all(temp)

print(count(temp))

L1 = SLList()
insert_after(L1, 2)
insert_after(L1, 5)
insert_after(L1, 7)

print_all(L1)

L2 = SLList()
insert_after(L2, 3)
insert_after(L2, 11)
print_all(L2)


L = merge_sorted_list(L1, L2)
print_all(L)
