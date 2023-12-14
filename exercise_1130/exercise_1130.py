class Student:

    #類別屬性
    schoolName = "南台科大"
    schoolAddress = "南台街1號"

    def __init__(self) -> None:
        pass

    #Instance屬性
    def __init__(self, id, major, credits, gpa, address):
        self._id = id
        self._major = major
        self._credits = credits
        self._gpa = gpa
        self._address = address
        
    def get_ID(self):
        return self._id

    def set_ID(self, value):
        self._id = value
    
    
    def get_schoolName(self):
        return self.schoolName

    def set_schoolName(self, value):
        self.schoolName = value

    def get_schoolAddress(self):
        return self.schoolAddress

    def set_schoolAddress(self, value):
        self.schoolAddress = value


#建立類別為Student的物件st1
st1 = Student("4B0G0038", "CSIE", 60, 4.00, "Da-Yan Rd. No. 124")
#呼叫副函式get_schoolName()
print(st1.get_schoolName())

#呼叫副函式get_ID()
print(st1.get_ID())