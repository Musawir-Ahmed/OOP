class Studen:
    def __init__(self, matric, inter):
        self.total = int(matric+inter)
    name = ""
    roll_no = ""
    total = ""


inter = int(input("ENTER  INTER MARKS ="))
matric = int(input("ENTER MATRIC MARKS ="))

s1 = Studen(inter, matric)
s1.roll_no = input("ENTER ROLL NO OF THE STUDENT =")

print(s1.roll_no, "\t", s1.total)
