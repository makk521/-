# %%
class Student:
    """
    The variable student_count is a class variable whose value is shared among all instances of a this class. 
    This can be accessed as Student.student_count from inside the class or outside the class.
    """
    student_count = 0
    """
    Initialize variables,if no input,there are default assignment
    """
    def __init__(self,name,age = 18):
        self.name = name
        self.age  = age
        Student.student_count += 1
        pass
    
    """
    Use variables defined using class initialization
    """
    def display_message(self):
        print(f"name : {self.name},age : {self.age}")
    
    """
    Change variables defined using class initialization
    """
    def change_age(self,new_age):
        self.age = new_age
    
    """
    Calling between functions in a class
    """
    def return_age(self):
        return self.age
    
    def display_age(self):
        age_temp = self.return_age()
        print(age_temp)


ma = Student('name1',19)
ka = Student('name2',16)
ma.display_message()
ka.display_message()
ma.display_age()

# %%
Student.student_count

# %%
#---------------------------------#
# Subclass inherits parent class  #
#---------------------------------#
class Student_Child(Student):
    def __init__(self, name, age=18):
        super().__init__(name, age)


ch = Student_Child('ming',11)
ch.display_age()

# %%
