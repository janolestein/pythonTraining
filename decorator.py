def decorator_with_arguments(function):
    def wrapper_accepting_arguments(*args, **kwargs):
        print("My arguments are: {0}, {1}".format(' '.join(map(str,args)),' '.join('{}={}'.format(k,v) for k,v in kwargs.items()))) #The format() method formats the specified value(s)
        function(*args, **kwargs)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

@decorator_with_arguments
def tester1():
    print("tester1: Ich habe keine Argumente")

@decorator_with_arguments
def tester2(ag1):
    print("tester2: {0}".format(ag1))

@decorator_with_arguments
def tester3(ag1,ag2,ag3):
    print("tester3: {0}, {1}, {2}".format(ag1,ag2,ag3))

tester1()          
tester2("a")
tester2(1)
tester3(1, ag2="Ich bin ein String", ag3=[1,2,[3]])
