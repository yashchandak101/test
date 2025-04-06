class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}



rect = Rectangle(10, 5)

print("Iterating over Rectangle instance:")
for item in rect:
    print(item)
