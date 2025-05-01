class SequenceIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start + 1

    def __iter__(self):
        return SequenceIterator(self.start, self.end)

class SequenceIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value

if __name__ == "__main__":
    start, end = 3, 10
    seq = SequenceIterable(start, end)  # Use SequenceIterable instead
    print(len(seq))
    for elem in seq:
        print("counting", elem)
    print(len(seq))
    for elem in seq:
        print("counting", elem)