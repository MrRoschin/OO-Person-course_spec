class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        return
    
    def printFullName(self):
        return
    
class Student(Person):
    def __init__(self, firstname, lastname, studentid, housegroup):
        super().__init__(firstname, lastname)
        self.studentid = studentid
        self.housegroup = housegroup
        self.subjects = []
        return

    def enrolClass(self, subjectname):
        s1 = self.Subject()
        s1.subjectname = subjectname
        s1.studentid = self.studentid
        return
    
class Subject():
    def __init__(self, studentid, subjectname):
        self.studentid = 0
        self.subjectname = ""
        return
    
    def printStudentList():
        return