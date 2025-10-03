class myClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return(f"Objek ini adaalah : {self.name}")
    def halo(self):
        print(f"Halo nama saya: {self.name}")
p1 = myClass("Pikachu",20)
print(p1.name)
print(p1.age)
print(p1)
p1.halo()


