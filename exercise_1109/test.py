def human(name,age):
    print(name,age)

def funcl(*nbr):
    for i in nbr:
        print(i)

def add_and_sub(a,b):
    print(a+b,a-b)

def show_employee(name,salary=9000):
    print(name , "salary:",salary)
def exercise5(a,b):
    a= a*a
    def a_add_b(a,b):
        return a+b
    anser = a_add_b(a,b)+5
    print(anser)

def exercise6(nbr):
    if (nbr!=0):
        return nbr + exercise6(nbr-1)
    else:
        return 0

def display_student(name, age):
    print(name,age)
display_student("emma",26)

human("Jason",20)
funcl(20,40,60)
funcl(80,100)
add_and_sub(40,10)
show_employee("Ben",12000)
show_employee("Jessa")
exercise5(5,10)
print(exercise6(10))
showStudent = display_student
print(showStudent("emma",21))
print(list(range(4,30,2)))
x = [4,6,8,24,12,2]
print(max(x))
print(min(x))