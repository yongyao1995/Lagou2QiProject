class Person:
    def __init__(self, name, age, gender):
        self.value= "fit"
        self.name = name
        self.age = age
        self.gender = gender

    def set_att(self, value):
        self.value = "fit"

    def eat(self):
        print(f" name : {self.name}, age : {self.age}, gender : {self.gender} 我在吃")

    def drink(self):
        print(f" name : {self.name}, age : {self.age} ， gender ： {self.gender} 我在喝")

    def run(self):
        print(f" name : {self.name} , age : {self.age} , gender: {self.gender} 我在跑")


xiaoming = Person("xiaoming", 10, 'male')
xiaohong = Person("xiaohong", 15, 'female')

print(xiaoming.name)
xiaoming.run()

xiaoming.set_att("fit")
print(xiaoming.value)
