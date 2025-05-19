class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printFullName(self):
        print(f"{self.firstname} {self.lastname}")
    
class Student(Person):
    def __init__(self, firstname, lastname, studentid, housegroup):
        super().__init__(firstname, lastname)
        self.studentid = studentid
        self.housegroup = housegroup
        self.subjects = []


    def enrolClass(self, subjectname):
        s1 = Subject(self.studentid, subjectname)
        self.subjects.append(s1)

    def printSubjects(self):
        print(f"")
    
class Subject():
    def __init__(self, studentid, subjectname):
        self.studentid = studentid
        self.subjectname = subjectname
    
    def printStudentList():
        pass
    
class Parent():
    def __init__(self, occupation, alumni):
        self.occupation = occupation
        self.alumni = alumni

Lucas = Student("Lucas", "Yang", "studentid", "housegroup")
Lucas.printFullName()
Lucas.enrolClass("Music")