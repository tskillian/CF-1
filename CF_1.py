class Library(object):
	def __init__(self):
		self.shelves = []
		self.all_books = []

	def add_shelf(self, shelf):
		self.shelves.append(shelf)

	def shelf_list(self):
		return self.shelves

	def add_book(self, title):
		self.all_books.append(title)

	def book_list(self):
		return self.all_books

class Shelf(object):
	def __init__(self, shelf_name, library):
		self.shelf_name = shelf_name
		self.library = library
		library.add_shelf(self.shelf_name)
		self.books_on_shelf = []

	def add_book(self, title):
		self.books_on_shelf.append(title)

	def remove_book(self, title):
		self.books_on_shelf.remove(title)

	def list_books_on_shelf(self):
		return self.books_on_shelf

class Book(object):
	def __init__(self, title, library):
		self.title = title
		library.add_book(self.title)

	def enshelf(self, shelf_name):
		shelf_name.add_book(self.title)

	def unshelf(self, shelf_name):
		shelf_name.remove_book(self.title)


# Creating a library, shelves, and books
best_library = Library()
fiction = Shelf('fiction', best_library)
non_fiction = Shelf('non fiction', best_library)
The_Hobbit = Book('The Hobbit', best_library)
Enders_Game = Book('Enders Game', best_library)
Fooled = Book('Fooled by Randomness', best_library)
# Use of enshelf method on books, shown to work when the books_on_shelf method is called
The_Hobbit.enshelf(fiction)
Enders_Game.enshelf(fiction)
Fooled.enshelf(non_fiction)

# The library is aware of its shelves (this returns fiction and non fiction)
print best_library.shelf_list()

# Each shelf knows what books it contains (Prints The Hobbit, Enders Game
# for fiction. Prints Fooled by Randomness for non fiction)
print fiction.list_books_on_shelf()
print non_fiction.list_books_on_shelf()

# The library has a method to report all books it contains
# (Prints The Hobbit, Enders Game, and Fooled by Randomness)
print best_library.book_list()

#To show that the unshelf method works
# Prints Enders Game
The_Hobbit.unshelf(fiction)
print fiction.books_on_shelf





