class Student:
    perc_rise = 0.5
    def __init__(self,first,last,marks,email):
        self.first= first
        self.last = last
        self.email = email
        self.marks = marks
    def fullname (self):

       return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.marks = int(self.marks* 1.05)


std_1 = Student('Abdul','Moiz', 70,'xyz@gmail.com')
std_2 = Student('Rushan', 'Rafiq',90,'xyz@gmail.com')


class Dumb(Student):
    perc_rise = 2

    def __int__(self,first,last,marks, prog_language):
        super().__init__(first,last,marks)
        self.prog_language =prog_language



std_2 = Dumb('Rushan', 'Rafiq',90,'python')

print(std_2.prog_language)








