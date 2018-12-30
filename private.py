class Person(object):
    def __init__(self):
        self.__age = 10
    #保证是可读属性
    @property
    def get_age(self):
        return self.__age

if __name__ == "__main__":
    person = Person()
    print(person.get_age)

