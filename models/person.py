class Person:
    def __init__(self,sno,name,city):
        self.sno=sno
        self.name=name
        self.city=city
    
    def __repr__(self):
        return str({'sno':self.sno,'name':self.name,'city':self.city})