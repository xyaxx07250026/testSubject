class MyHashMap(object):
    def __init__(self):
      self.KEYS = []
      self.DELETED = -1
      self.m=0
      self.T= [None]
      
    def put(self):
      self.KEYS = eval(input("输入字符串数组："))
      self.m = len(KEYS)
      self.T = [None for _ in range(m)]
      
    def h1(self,k):
      return k % m
 
    def HASH_INSERT(self,k):
        j=self.h1(k)
        if self.T[j] == None or self.T[j]==self.DELETED:
            self.T[j]=k
            return j
 
    def HASH_SEARCH(self,k):
        j=self.h1(k)
        if self.T[j] == k:
                return j
 
        if self.T[j] == None:
                return None
 
    def HASH_DELETE(self,k):
        i=self.HASH_SEARCH(k)
        if i is None:
            raise Exception("key %s doesn't exist"%k)
        self.T[i] = self.DELETED
 
if __name__=='__main__':
    hash = MyHashMap()
    hash.put()
    for k in hash.KEYS:
        hash.HASH_INSERT(k)
    print "all keys:"
    print(hash.T)
 
    print "every key:"
    for k in hash.KEYS:
        print(k,hash.HASH_SEARCH(k))
 
    print "del key1:"
    hash.HASH_DELETE(KEYS[1])
    print(hash.T)
 
    print "none keys:"
    for k in hash.KEYS:
        if hash.HASH_SEARCH(k) is None:
            print(k)
 
    print "insert key1:"
    hash.HASH_INSERT(hash.KEYS[1])
    print(hash.T)
