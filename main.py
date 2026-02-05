class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def get_description(self):
        return f"{self.title} (ID: {self.item_id})"
    
    def can_borrow(self):
        return True

book = LibraryItem("Neuromancer", "N123")

print(book.can_borrow())