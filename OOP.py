class person:
    def __init__(self):
        self.name='Suleiman umar farouk'
        self.age=23
        self.location='Abuja,Nigeria'
    def talk(self):
        print('My name is',self.name)
    def vote(self):
        if self.age>18:
            print('i am eligible to vote')
        else:
            print('i am not eligible to vote')        

obj1=person()

obj1.talk()
obj1.vote()


     
        
    