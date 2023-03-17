class AlgoHashTable:

    def __init__(self, size): # constructor used to create the hash table object
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)] # creating many mini lists within one big lists

    def set_val(self, key, value): # insert records consisting of key value pairs
        hashed_key = hash(key)%self.size # The mod of the size of buckets is used to produce a index value that is within the range of the size
        bucket = self.hash_table[hashed_key] # points to the bucket where the key andvalue will be stored
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key: # if the key passed in already exists in the bucket
                found_key = True
                break # break out to save the index
        if found_key: # if key exists
            bucket[index] = (key, value) # update the item by referencing the index and set the bucket to the key and value passed in
        else:
            bucket.append((key, value)) # append the tuple to the end of the list as a new record

    def get_val(self,key): # search method
        hashed_key = hash(key)%self.size 
        bucket = self.hash_table[hashed_key] 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key: 
                found_key = True
                break 
        if found_key:
            return record_value
        else:
            return "No record found with that email address"
    
    def __str__(self): # method called when we try to print the hash table 
        return "".join(str(item) for item in self.hash_table) # return a string representation of each minilist 
    
hash_table = AlgoHashTable(256) # creating a new hash table object and passing in the size
with open("data.txt") as f:# read in data from the file
    for line in f:
        key, value = line.split(":") # separate each line in the file into key and value
        hash_table.set_val(key, value) # adding the key and value to the hash table

print(hash_table.get_val("crshaka@example.com"))
print(hash_table.get_val("craig@example.com"))