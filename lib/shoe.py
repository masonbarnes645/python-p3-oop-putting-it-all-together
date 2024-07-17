#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        self.size = size
    def get_condition(self):
        return self._condition
    def set_condition(self, condition):
        self._condition = condition
    def cobble(self):
         self.condition = "New"
         print("Your shoe is as good as new!")
    def set_size(self, size):
        if not isinstance(size, int):
            self._size = None
            print("size must be an integer")               
        else:
            self._size = size
    def get_size(self):
        return self._size 
    
    condition = property(get_condition, set_condition)
    size = property(get_size, set_size)


blank = Shoe('nike', '12')

print(blank)