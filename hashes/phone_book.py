from custom_hashtable import HashTable

class PhoneBook():

    def __init__(self, no_of_entries):
        self.hash_table = HashTable(no_of_entries)
    
    def insert(self, key, value):
        self.hash_table.insert(key, value)

    def get(self, key):
        val = self.hash_table.get(key)
        if val:
            return "{} = {}".format(key, val)
        return "Not Found"

if __name__ == "__main__":
    no_of_entries = 3
    phone_book1 = PhoneBook(no_of_entries)
    phone_book1.insert("sam", 99912222)
    phone_book1.insert("tom", 11122222)
    phone_book1.insert("harry", 12299933)

    print(phone_book1.get("sam"))
    print(phone_book1.get("edward"))
    print(phone_book1.get("harry"))
