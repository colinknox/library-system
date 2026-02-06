class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def get_description(self):
        return f"{self.title} (ID: {self.item_id})"
    
    def can_borrow(self):
        return True
    
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self._is_checked_out = False

    def checkout(self):
        if self._is_checked_out == True:
            raise Exception("Book is already checked out")
        else:
            self._is_checked_out = True




book = LibraryItem("Neuromancer", "N123")
hobbit = Book("The Hobbit", "H321", "J. R. R. Tolkien")

print(hobbit._is_checked_out)
print(hobbit.checkout())
print(hobbit._is_checked_out)




