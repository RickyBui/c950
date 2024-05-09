# Create Hash Table
class CreateHashMap:
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Time Complexity O(1) and Space Complexity O(1)
    # Inserts a new item into the hash table
    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket already
        for kv in bucket_list:  # O(N) CPU time
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Time Complexity O(N) for number of element in list Space Complexity O(1)
    # Lookup items in hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None  # no pair[0] matches key 0

    # Same Time and Space Complexity as lookup
    # Hash remove function - removes item from hash table
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key exist in the hash table then remove the item
        if key in destination:
            destination.remove(key)

    def list_all(self):
        print(self.list)
        return self.list

#Check to make sure items are properply added onto hash table
#myHash = CreateHashMap(20)
#myHash.insert('apple', ' apple')
#print(CreateHashMap(20))
#print(myHash.lookup('apple'))
#print(myHash.hash_remove('apple',))
#print(myHash.lookup('orange'))
#print(myHash.list_all())