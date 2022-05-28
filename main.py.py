class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name="Bob", age=26,track=["FE","BE"], score=20.90):
        self.name= str(name)
        self.age= int(age)
        self.track =str(track)
        self.score= float(score)

    def change_name(self, change_name):
        self.name= change_name
        print("The student new name is ", self.name)

    def change_age(self, change_age):
        self.age = change_age
        f = isinstance(change_age, int)
        print("The student new age is ", self.age)
        
    def add_track(self, add_track):
        self.track = add_track
        print("The student new track is ", self.track)
    
    def get_score(self):
        print(self.score)



Bob = Student("Bob",26,["FE","BE"],20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
