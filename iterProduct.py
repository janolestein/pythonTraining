import itertools as itertools
from contextlib import contextmanager


colorOptions = [1, 2, 3, 4, 5, 6, 7, 8]
allSolutions = set(itertools.product(colorOptions, repeat=5))
print(str(len(allSolutions)))

class DateiAppender:
    def __init__(self, file_name):
        self.file_name = file_name
    
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, "w")
            yield file
        finally:
            file.close()


dateiappender = DateiAppender("product.txt")
with dateiappender.open_file() as file:
    file.write(str(allSolutions))

