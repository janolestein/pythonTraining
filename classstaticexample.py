class Example():
    
    @staticmethod
    def static_method(*args):
        return args
    
    @classmethod
    def class_method(*args):
        return args

obj = Example()

print('Aufruf von static_method:',obj.static_method())
print('Aufruf von class_method:',obj.class_method())
# Der Pyhton Interpreter scheint die Klasse automatisch als Argument zu übergeben, ich kann aber leider keine Dokumentation dazu finden die das bestätigt.  
