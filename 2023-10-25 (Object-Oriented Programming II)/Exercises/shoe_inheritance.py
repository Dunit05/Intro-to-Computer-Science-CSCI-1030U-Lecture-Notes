class Product:
    def __init__(self, price, description):
        self._price = price
        self._description = description


class Shoe(Product):
    def __init__(self, brand, size, colour, price, description):
        super().__init__(price, description)
        self._brand = brand
        self._size = size
        self._colour = colour

    def __str__(self):
        return f"Brand: {self._brand}; Size: {self._size}; Colour: {self._colour}; (Price: ${self._price})"


shoe = Shoe("Nike", 10, "Black", 100, "Running shoe")
print(shoe)
