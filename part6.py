class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._has_next = None
        self._next_item = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._has_next is None:
            self._next_item = next(self.iterator)
        self._has_next = None
        return self._next_item

    def peek(self):
        if self._has_next is None:
            try:
                self._next_item = next(self.iterator)
                self._has_next = True
            except StopIteration:
                self._has_next = False
        if not self._has_next:
            raise StopIteration
        return self._next_item

    def has_next(self):
        if self._has_next is None:
            try:
                self._next_item = next(self.iterator)
                self._has_next = True
            except StopIteration:
                self._has_next = False
        return self._has_next
