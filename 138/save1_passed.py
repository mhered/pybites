from pprint import pprint

class Animal:
    sequence=10000
    animals = []
    
    def __init__(self, name):
        self.__class__.sequence +=1
        self.id = self.__class__.sequence
        self.name  = name.title()
        self.__class__.animals.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"
        
    @classmethod
    def zoo(cls):
        return "\n".join([str(item) for item in cls.animals])
            