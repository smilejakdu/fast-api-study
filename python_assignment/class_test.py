class Student:
    def __int__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name}'

    def fullname_with_school(self):
        return f"{self.major} {self.school}"

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        # https: // wikidocs.net / 16074
        # @classmethod 는 정적 메서드이다.
        first_name, last_name, major = student_str.split(".")
        return cls(first_name, last_name, major)


class ColleageStudent(Student):
    def __int__(self, first_name, last_name, major):
        super().__int__(first_name, last_name)
        self.major = major


class NonColleageStudent(Student):
    def __int__(self, first_name, last_name, future_adult_job):
        super().__int__(first_name, last_name)
        self.future_adult_job = future_adult_job

    def grow_up(self):
        return f"When I grow up, I want to be a {self.future_adult_job}"


student_1 = ColleageStudent("robert", "ahn", "math")
student_2 = Student("dami", "jun")
print(student_2.major)

print(student_1.fullname_with_major())
print(student_2.fullname_with_major())
new_student = "new student"
student_3 = Student.split_students(new_student)
print(student_3.fullname_with_major())
