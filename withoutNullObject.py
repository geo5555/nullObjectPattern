Persons = {}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(self.name, self.age)

def createPersons():
    for i in range(10):
        p = Person(f'name{i}', 20+i)
        Persons[i] = p

if __name__ == '__main__':
    createPersons()
    for i in range(5,11):
        p = Persons.get(i)
        if p is not None:
            p.printPerson()
        else:
            print("no such person")