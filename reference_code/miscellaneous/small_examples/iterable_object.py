class InclusiveRange:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    
    def __iter__(self):
        return self # the object having __next__ method
    
    def __next__(self):
        if self.low <= self.high:
            self.low += 1
            return self.low - 1
        else:
            raise StopIteration()
        
for num in InclusiveRange(1,3):
    print(num)