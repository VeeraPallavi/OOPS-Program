class Student:
    """
    Student Management
    Create a Student class where:
    Student ID, name, and marks are private
    Provide getter and setter methods
    Validate that marks are between 0 and 100
    """
    def __init__(self, id, name):
        self.__id = id 
        self.__name = name
        self.__marks = 0

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if(0 <= marks <= 100):
            self.__marks = marks
        else:
            print("Invalid marks")

student1 = Student(1, "Jhon")
student1.set_marks(101)
print(student1.get_id()) 
print(student1.get_name())
print(student1.get_marks())   
        