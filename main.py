import requests
import hashlib

class cracker():
    def __init__(self, hash):
        self.hash = hash
        self.hash_type = None
    def hash_type_checker(self):
        Hash = self.hash
        resault = None
        if len(Hash) == 32:
            self.hash_type = 'md5' # md5 32 char
        elif len(Hash) == 64:
            self.hash_type = 'sha256' #sha256 64 char
        elif len(Hash) == 56:
            self.hash_type  = 'sha224' #sha224 120 char
        else:
            return "this app does not support type of your hash!!!"
        return self.hash_type
    def checker(self):
        Hash = self.hash
        Hash_type = self.hash_type_checker()

        s = requests.get(f"http://localhost:8000/hash_checker/{self.hash}/{self.hash_type}")
        
        resault = s.json()
        return resault["word"]
        
if __name__ == "__main__":
    while True:
        Hash = input("please enter your hash: ")
        my_checker = cracker(Hash)
        while my_checker.hash_type_checker() == "this app does not support type of your hash!!!":
            print("this app does not support type of your hash!!!")
            Hash = input("please enter your hash: ")
            my_checker = cracker(Hash)
        print(f"your hash type is : {my_checker.hash_type_checker()}")
        print(my_checker.checker())










#Winchesterage | kian beh