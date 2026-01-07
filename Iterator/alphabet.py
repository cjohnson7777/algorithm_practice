
# CONCRETE ITERATOR
class AlphabeticalOrderIterator:
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            # Signal that the iteration is finished
            raise StopIteration()

# CONCRETE COLLECTION
class WordsCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        # Return a new iterator object
        return AlphabeticalOrderIterator(self._items)

# CLIENT
collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

for item in collection:
    print(item)
