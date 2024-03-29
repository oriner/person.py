class person:
 def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender

    def introduce(self):
        print("Hi, my name is{self.name}.I am {self.age}years old and I am {self.gender}")

        person=person("Lavendah",22,"Female")
        person.introduce()