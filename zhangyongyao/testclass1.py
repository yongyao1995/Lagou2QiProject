class Person():
    name ="noname"

    def get_name(self):
        return self.name

print(Person.name)

p =Person()
print(p.name)
print(p.get_name())

Person.name ='lili'
p.name = 'xiaoming'
print(p.name)