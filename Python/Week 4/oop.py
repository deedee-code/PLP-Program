class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def Introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")


introducePerson = Person("Doris", 24, "Female")

introducePerson.Introduce()