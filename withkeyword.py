class DateiAppender:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "a")
        return self.file
    def __exit__(self, *args):
        self.file.close()

with open('datei.txt', mode = 'a') as appender:
    appender.write('Ein Eintrag in die Datei!')

with DateiAppender("datei.txt") as file1:
    file1.write("\nIst das nun das Ende?")
