class square_generator:
    def __init__(self, start_num, end_num):
        self.start_num = start_num
        self.end_num = end_num
        self.current_num = start_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num > self.end_num:
            raise StopIteration
        else:
            self.current_num += 1
            return self.current_num**2


print(list(square_generator(5, 10)))
