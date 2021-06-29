"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.increment = start
        self.initalized = False
    
    def generate(self):
        if not self.initalized:
            self.initalized = True
            return self.start
        else:
            self.increment += 1
            return self.increment

    def reset(self):
        self.increment = self.start
        self.initalized = False