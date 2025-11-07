#!/usr/bin/env python3


class Coffee:
    """
    A class representing a coffee with size and price.
    """

    _ALLOWED_SIZES = {"Small", "Medium", "Large"}

    def __init__(self, *, size, price):
        self._size = None
        self.size = size  # route through setter for validation
        self.price = float(price)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in self._ALLOWED_SIZES:
            self._size = value
        else:
            # Do not change the existing value; just print the required message.
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Exact punctuation matters for the test (note the curly apostrophe).
        print("This coffee is great, here’s a tip!")
        self.price += 1
