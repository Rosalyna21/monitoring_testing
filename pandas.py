class Panda:
    def __init__(self,name, age):
        assert name.isalnum()
        assert len(name)>3 and len(name)<=25
        assert isinstance (age, init)
        assert age>0 and age <=100
        self.name=name
        self.age=age
        self.hunger=50

    def __str__(self):
        return f"[Nom:{self.name}/Age:{self.age}/Faim:{self.huner}/100]"
    


