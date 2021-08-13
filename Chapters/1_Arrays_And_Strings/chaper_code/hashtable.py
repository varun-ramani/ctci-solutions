# HashMap from scratch
class HashMap:
    def __init__(self, capacity=100):
        self.underlying_list = [None] * capacity
        self.capacity = capacity

    def get_hash_index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        hash_index = self.get_hash_index(key)

        if self.underlying_list[hash_index] is None:
            self.underlying_list[hash_index] = [[key, value]]
        else:
            for pair in self.underlying_list[hash_index]:
                if pair[0] == key:
                    pair[1] = value
                    return

            self.underlying_list[hash_index].append([key, value])
            
    def get(self, key):
        hash_index = self.get_hash_index(key)

        if self.underlying_list[hash_index] is not None:
            for table_key, table_value in self.underlying_list[hash_index]:
                if key == table_key:
                    return table_value
        return None

# HashMap using a dictionary
my_map = {}