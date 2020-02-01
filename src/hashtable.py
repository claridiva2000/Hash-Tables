# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity=10):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage =[[] for _ in range(0, self.capacity)]
        self.count =0 
        # if self.count > self.capacity-1:
        #     self.capacity = self.capacity *2   
        # print(self.capacity)     

    def hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hashed = 0
        for letter in str(key):
            hashed= hashed + ord(letter) 
        
        res= hashed % self.capacity
        
        return res




#     def _hash_djb2(self, key):
#         '''
#         Hash an arbitrary key using DJB2 hash

#         OPTIONAL STRETCH: Research and implement DJB2
#         '''
#         pass


#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_key = self.hash(key)
        key_exists = False
        bucket = self.storage[hashed_key]
        
        
        for i,kv in enumerate(bucket):
            k,v = kv
            if key == k:
                key_exists = True
        if key_exists:
            bucket[i] = ((key,value))
            
        else:
            bucket.append((key, value))
            self.count +=1
            print(f' buckets filled: {self.count}')

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self.hash(key)
        key_exists = False
        bucket = self.storage[hashed_key]
        for i,kv in enumerate(bucket):
            k,v = kv
            if key == k:
                key_exists = True
        if key_exists:
            print(f'deleted {bucket[i]}')
            del bucket[i] 
            self.count -= 1
            

        else:
            print('key does not exist')
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self.hash(key)
        bucket = self.storage[hashed_key]
        for kv in bucket:
            k,v = kv
            if key == k:
                return v
            else:
                raise KeyError('does not exist')


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        if self.count >= self.capacity-1:
            self.capacity = self.capacity*2
        


H = HashTable()
H.insert('key1', 'val1')
H.insert('key2', 'val2')
H.insert('key3', 'val3')
H.insert('key4', 'val4')
H.insert('key5', 'val5')
H.insert('key6', 'val6')
H.insert('key7', 'val7')
H.insert('key8', 'val8')
H.insert('key9', 'val9')
H.insert('key10', 'val10')
H.insert('key11', 'val11')
H.insert('key12', 'val12')
H.insert('key13', 'val13')

print(H.retrieve('key1'))
H.remove('key2')

print(H.storage)

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
