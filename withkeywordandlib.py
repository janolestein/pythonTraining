from contextlib import contextmanager

class DateiAppender:
    def __init__(self, file_name):
        self.file_name = file_name
    
    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, "a")
            yield file
        finally:
            file.close()


dateiappender = DateiAppender("datei.txt")
with dateiappender.open_file() as file:
    file.write("Das Ende ist fern")
