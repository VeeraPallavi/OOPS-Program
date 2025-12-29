class Father:
    def skills(self):
        print("Father")

class Mother:
    def skills(self):
        print("Mother")

class Child(Father, Mother):
    def child_skills(self):
        print("Child Class")
    
child = Child()
child.child_skills()
child.skills()

