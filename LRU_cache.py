# https://leetcode.com/problems/lru-cache/solutions/

# this works but i guess it's not fast
# apparently there's comething caled ordered dict in python that makes this faster
# or just use python dict since
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.age = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache[key][1] = self.age
            self.age += 1
            return self.cache[key][0]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
    

        # evict
        if len(self.cache)==self.capacity and key not in self.cache:
            # find least recently used
            min_age = [0, 10000000]
            for k in self.cache:
                if self.cache[k][1] < min_age[1]:
                    min_age = [k, self.cache[k][1]]
            # delete least recently used
            del self.cache[min_age[0]]

            # add new one, woth fresh age
            self.cache[key] = [value, self.age]
            self.age += 1

        else:
            self.cache[key] = [value, self.age]
            self.age += 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)