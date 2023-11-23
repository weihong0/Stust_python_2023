class Employee():
    def __init__(emp,id,name,salary,department):
        emp.id =id
        emp.name = name
        emp.salary = salary
        emp.department = department

    def calculate_emp_salary(emp,work_hr):
        if work_hr>50:
            new_salary=emp.salary+(work_hr-50)*(emp.salary/50)
        else:
            new_salary=emp.salary
        print(new_salary)

    def emp_assign_department(emp,new_department):
        emp.department =new_department
        
    def print_employee_details(emp):
        print(f"Employee ID: {emp.name}")
        print(f"Employee Name: {emp.id}")
        print(f"Employee Salary: {emp.salary}")
        print(f"Employee Department: {emp.department}")

adams = Employee(id="E7876",name="Adams",salary=50000,department="ACCOUNTING")
jones = Employee(id="E7499",name="Jones",salary=45000,department="RESEARCH")
martin = Employee(id="E7900",name="Martin",salary=50000,department="SALES")
smith = Employee(id="E7698",name="Smith",salary=55000,department="OPERATIONS")

adams.print_employee_details()
adams.emp_assign_department("RESEARCH")
adams.print_employee_details()
adams.calculate_emp_salary(80)
adams.calculate_emp_salary(25)