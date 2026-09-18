class Node:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummyhead = Node(-1, -1) # LRU
        self.dummytail = Node(-2, -2)

        self.dummyhead.nxt = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.cache = {} # key : node as value

    def _remove(self, node):
        # ->
        prev_node = node.prev
        prev_node.nxt = node.nxt
        # <-
        nxt_node = node.nxt
        nxt_node.prev = prev_node

    def _insert(self, node):
        #
        tail_node = self.dummytail.prev
        # 
        tail_node.nxt = node
        node.prev = tail_node
        node.nxt = self.dummytail
        self.dummytail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        # lookup key, if exits, update node
        if key in self.cache:
            old_node = self.cache[key]
            self.cache[key] = node # update the value node
            # remove the old node with the key
            self._remove(old_node)
            # insert the new node with the key and value
            self._insert(node)

        else: # key not exits, insert node, 
            # insert new node
            self.cache[key] = node 
            self._insert(node)

            # check the capacity
            if len(self.cache) > self.capacity:
                # evict if cache is full
                head = self.dummyhead.nxt
                evict_key = head.key
                self.cache.pop(evict_key)
                self._remove(head)
                



        




        
