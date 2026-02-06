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
        self.__is_checked_out = False

    def checkout(self):
        if self.__is_checked_out == True:
            raise Exception("Book is already checked out")
        else:
            self.__is_checked_out = True

    def return_item(self):
        self.__is_checked_out = False
    
    def is_available(self):
        if self.__is_checked_out == False:
            return True
        else:
            return False

class DVD(LibraryItem):
    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes
        self.__is_check_out = False

    def checkout(self):
        if self.__is_check_out == True:
            raise Exception("DVD is already checked out")
        else:
            self.__is_check_out = True

    def return_item(self):
        self.__is_check_out = False

    def is_available(self):
        if self.__is_check_out == False:
            return True
        else:
            return False

class ReferenceBook(LibraryItem):
    def __init__(self, title, item_id, subject):
        super().__init__(title, item_id)
        self.subject = subject

    def can_borrow(self):
        return False
    
    def checkout(self):
        raise Exception("Reference books cannot be checked out")

# book = LibraryItem("Neuromancer", "N123")
# hobbit = Book("The Hobbit", "H321", "J. R. R. Tolkien")
# batman = DVD("Batman", "B246", 126)

reference = ReferenceBook("Test Book", "T837", "Non-Fiction")

print(reference.can_borrow())
print(reference.checkout())