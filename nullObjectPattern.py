Persons = {}

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(self.name, self.age)

class NullPerson():
    def __init__(self):
        self.name = "no such person"
        #self.age = "no age"
    
    def printPerson(self):
        print(self.name)

def createPersons():
    for i in range(10):
        p = Person(f'name{i}', 20+i)
        #Persons.update({i : p})
        Persons[i] = p
        #p.printPerson()

def getPerson(id):
    try:
        return Persons[id]
    except KeyError:
        return NullPerson()

if __name__ == '__main__':
    createPersons()
    for i in range(5,11):
        p = getPerson(i)
        print(type(p))
        p.printPerson()

