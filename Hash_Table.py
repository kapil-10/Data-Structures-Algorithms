class hash_table: # hash_table without collision
    def __init__ (self):
        self.arr = []
        for value in range(100):
            self.arr.append(None)

    def get_hash(self,key):
        sum = 0 
        for value in key:
            sum += ord(value)
        return sum % 100
    
    def __setitem__(self,key,value): # we can use opeartor funcations instead of funcation name add 
        hk = self.get_hash(key)
        self.arr[hk] = value

    def __getitem__(self,key): # we can use opeartor funcations instead of funcation name search
        hk = self.get_hash(key)
        return self.arr[hk]
    
    def __delitem__(self,key): # we can use opeartor funcations instead of funcation name delete
        hk = self.get_hash(key)
        self.arr[hk] = None
    
    def print(self):
        for key,value in enumerate(self.arr):
            if value is not None:
                print('The index is ',key,'The value is ',value)



class hash_table_with_collision: # hash_table with collision
    def __init__ (self):
        self.arr = []
        for value in range(100):
            self.arr.append([]) 

    def get_hash(self,key):
        sum = 0 
        for value in key:
            sum += ord(value)
        return sum % 100
    
    def __setitem__(self,key,value): 
        hk = self.get_hash(key)
        found = False
        for index,value in enumerate(self.arr[hk]):
            if len(value) == 2 and value[0] == key:
                self.arr[hk] [index] = (key,value)
                found = True 
                break
        if not found:
            self.arr[hk].append((key,value))

    def __getitem__(self,key): 
        hk = self.get_hash(key)

        for element in self.arr[hk]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key): 
        hk = self.get_hash(key)
        for index,element in enumerate(self.arr[hk]):
            if element[0] == key:
                del self.arr[hk] [index]
    
    def print(self):
        for key,value in enumerate(self.arr):
            if value is not None:
                print('The index is ',key,'The value is ',value)


if __name__ == '__main__':
    input = 'kapil'
    hash = hash_table()
    hash['kapil'] = 1997
    hash['verma']= 2024
    hash['master_software_developer'] = 2023
    hash['kapil']
    hash.print()
    del hash['kapil']
    hash.print()

    input = 'kapil'
    hashwc = hash_table_with_collision()
    hashwc['kapil'] = 1997
    hashwc['kapil'] = 2019
    hashwc['verma']= 2024
    hashwc['dob'] = 1997
    hashwc['birth month'] = 9
    hashwc['master_software_developer'] = 2023
    hashwc.print()
    print('')
    hashwc['kapil']
    hashwc['verma']
    hashwc.print()
    print('')
    del hashwc['kapil']
    hashwc.print()


