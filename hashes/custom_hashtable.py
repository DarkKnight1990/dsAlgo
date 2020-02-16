"""
    Hash Table Implementation in Python
"""


class HashTable():

    def __init__(self, len):
        self.len = len
        self.hash_table = [[] for _ in range(len*2)]

    def _hash_func(self, key):
        return hash(key) % self.len

    def insert(self, key, value):
        hash_key = self._hash_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_key = self._hash_func(key)
        bucket = self.hash_table[hash_key]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = self._hash_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted.'.format(key))
        else:
            print('Key {} not found'.format(key))


if __name__ == "__main__":
    hash_table = HashTable(10)
    print(hash_table)
    hash_table.insert('a', 'Apple')
    hash_table.insert(10, 'First 2 digit number')
    hash_table.insert('10', 'Why converted to String')
    hash_table.insert('dolphin', 'They are cute')

    print(hash_table.hash_table)

    print(hash_table.get(10))
    print(hash_table.get('10'))

    hash_table.delete(10)
    print(hash_table.get(10))
    print(hash_table.hash_table)
