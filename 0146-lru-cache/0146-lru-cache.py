class Node:
    
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mp={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next,self.right.prev  = self.right,self.left #make dummy nodes for LRU (left) Most RU(right)
        
    def remove(self,node):
        node.prev.next, node.next.prev = node.next ,node.prev
    
    def insert(self,node):
        node.next, node.prev = self.right, self.right.prev
        self.right.prev,node.prev.next=node, node
        

    def get(self, key: int) -> int:
        # print("get",self.left.next.val,self.right.prev.val)
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            # print("after get",self.left.next.val,self.right.prev.val)
            return self.mp[key].val # as value of map is node
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print("before put",self.left.next.val,self.right.prev.val)
        n=Node(key,value)
        if key not in self.mp:
            self.mp[key]=n
            self.insert(n)
        else:
            self.remove(self.mp[key])
            self.mp[key]=n
            self.insert(n)
        if len(self.mp)>self.cap:
            del self.mp[self.left.next.key]
            self.remove(self.left.next)
        # print("after put",self.left.next.val,self.right.prev.val)
            
        
            
        
        

# We could have used OrderedDict for this as it keeps track of the order in which eles are inserted and we just keep reinserting while accessing.

# For interview: OrderedDict is internally implemented as Doubly linked list and hashmap so we will do the same 