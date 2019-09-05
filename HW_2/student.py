import sys

class Student(object):
    def __init__(self, name, age, gpa):
        self.name = name
        self.gpa = gpa
        self.age = age

    # Returns the name of the student as a string
    def __str__(self):
        return '{self.name}'.format(self=self)

    # The only thing sorted on in this class is name
    def __lt__(self, other):
        if self.gpa == other.gpa:
            if self.name == other.name:
                return self.age < other.age
            else:
                return self.name < other.name
        else:
            return self.gpa < other.gpa

    # Compares all class fields
    def __eq__(self, other):
        return self.gpa == other.gpa \
               and self.name == other.name \
               and self.age == other.age

    # Key for use in hashing this object
    # Learned how to do this from
    # https://stackoverflow.com/a/2909119
    def __key(self):
        return (self.name, self.gpa, self.age)

    # Returns the hash of the key for this object
    def __hash__(self):
        return hash(self.__key())