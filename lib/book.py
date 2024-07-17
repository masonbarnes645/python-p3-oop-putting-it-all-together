#!/usr/bin/env python3

class Book:
    def __init__(self,title, page_count) -> None:
        self.title = title
        self.set_page_count(page_count)
       
    def turn_page(self):
         print("Flipping the page...wow, you read fast!")
    def set_page_count(self,page_count):
        if not isinstance(page_count, int):   
                print("page_count must be an integer")             
        else:
            self._page_count = page_count
    def get_page_count(self):
        return self._page_count
        
    
    page_count = property(get_page_count, set_page_count)
       
newbook = Book('sds', '123')

print(newbook)


