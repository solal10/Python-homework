import itertools
import sys


class Course:
    def __init__(self, tempname):
        """
        constructor of the course class
        build an object of the course type with only name and set the grade at 101 (which means the grade as not been set yet)
        :param tempname: name of the course received form the file/user
        """
        self.name = tempname
        self.grade = 101

    def setGrade(self, tempgrade):
        """
        set the grade of the course only if its between 0 and 100
        :param tempgrade:the grade received from the file/user
        :return: no return value
        """
        if 0 <= int(tempgrade) <= 100:
            self.grade = tempgrade

    def getGrade(self):
        """
        allows to get the grade of a course
        :return: grade as an integer
        """
        return int(self.grade)

    def getName(self):
        """
        allows to get the name of the course
        :return:  the name of the course
        """
        return self.name

    def __str__(self):
        return f' course:{self.name} {self.grade}'

    def __repr__(self):
        return f' course:{self.name} {self.grade}'


class Student:
    def __init__(self, tempname, tempID):
        """
        constructor of the student class
        build an object of the type student with a name an ID and a empty list of courses (list of object of type course)
        :param tempname: name received from the file or the user
        :param tempID:  ID received from the file or the user
        """
        self.name = tempname
        self.__ID = tempID
        self.courses = []

    def getID(self):
        """
        allows to get the ID of the student
        :return: ID of the student
        """
        return self.__ID

    def getcourses(self):
        """
        allows to get the list of the course of the student
        :return: list of course objects
        """
        return self.courses

    def addCourse(self, coursename, coursegrade):
        """
        allow to add a course to the list of courses of the student
        the method check if the courses is already in the list than swap between the grades if the new one is valid
        otherwise the method check if the grade is valid (between 0 and 100 ) if yes the method builds a course type
        object and than adds it to the student list of courses.
        :param coursename: Name of the course received from the file or the user
        :param coursegrade: grade of the student in the course received from the file or the user
        :return:
        """
        for i in range(len(self.courses)):
            if self.courses[i].getName() == coursename:
                if 0 <= int(coursegrade) <= 100:
                    newcourse = Course(coursename)
                    newcourse.setGrade(coursegrade)
                    self.courses[i] = newcourse
                    return
        if 0 <= int(coursegrade) <= 100:
            newcourse = Course(coursename)
            newcourse.setGrade(coursegrade)
            self.courses.append(newcourse)

    def getname(self):
        """
        allos to get the name of the student
        :return: name of the student
        """
        return self.name

    def __str__(self):
        return f'name:{self.name} ID:{self.__ID} courses:{self.courses}'

    def __repr__(self):
        return f'name:{self.name} ID:{self.__ID} courses:{self.courses}'

    def calcavg2(self):
        """
        a method that calculate the average of the student if he have take courses (otherwhise return NO COURSE TAKEN
        instead of the average ) and then returns a format (ID: studentID average: studentaverage)
        :return: a string format to help write in the output file
        """
        if len(self.courses) == 0:
            return f'ID:{self.getID()} NO COURSE TAKEN\n'
        listgrade = list(map(lambda obj: obj.getGrade(), self.courses))
        avg = sum(listgrade) / len(listgrade)
        return f'ID:{self.getID()} average:{avg}\n'


filename = input("Enter the name of the data file you wish to open (with the extension of the file)\n")
try:
    f = open(filename, 'r')
    students = []
    i = 0
    for line in f:
        line = line.rstrip()
        tempstudent = list(line.split("\t"))
        students.append(Student(tempstudent[0], tempstudent[1]))
        tempcourse = tempstudent[2].split(";")
        for j in range(len(tempcourse)):
            temp = tempcourse[j].split("#")
            students[i].addCourse(temp[0], temp[1])
        i += 1
    f.close()
except OSError as err:
    print(f"OS error: {err}.")
    sys.exit()
if len(students) == 0:
    print("No student in the database\n")
    sys.exit()
i = 0
while i != 4:
    i = int(input(
        "1) calulate a student average \n2) calculate average grade in a course \n3) calculate the average of all students \n4) exit the system\n"))
    if i == 1:
        avgstudent = input("enter the name of the student you wish to calculate the average\n")
        student = list(filter(lambda obj: obj.getname() == avgstudent, students))
        print(student[0].calcavg2())

    if i == 2:
        oldlistcourse = list(map(lambda obj: obj.getcourses(), students))
        listcourse = list(itertools.chain(*oldlistcourse))
        coursename = input("enter the name of the course you wish to calculate the average\n")
        listgrade = list(filter(lambda obj: obj.getName() == coursename, listcourse))
        listgrade = list(map(lambda obj: obj.getGrade(), listgrade))
        if len(listgrade) != 0:
            sumgrade = sum(listgrade)
            numofgrade = len(listgrade)
            avg = sumgrade / numofgrade
            print(coursename, ":", avg, '\n')
        else:
            print("no student took this course\n")
    if i == 3:
        try:
            filename2 = input("Enter the name of the output file you wish to open (with the extension of the file)\n")
            f = open(filename2, 'w')
            listavg = list(map(lambda obj: obj.calcavg2(), students))
            string1 = ""
            stringavg = string1.join(listavg)
            f.write(stringavg)
            f.close()
        except OSError as err:
            print(f"OS error: {err}.")
            sys.exit()
    if i == 4:
        print("thank tou goodbye\n")
        sys.exit()
