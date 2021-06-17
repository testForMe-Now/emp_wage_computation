import random


class Employee:
    def __init__(self, emp_name, emp_id, department, form, check):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.department = department
        self.work_type = form
        self.is_present = check

    def check_emp_present_or_absent(self):
        random_num = random.randint(0, 1)
        if random_num == self.is_present:
            return True
        else:
            return False

    def calculate_monthly_wage(self):

        emp_wage = 0
        count = 0
        while True:
            count += 1
            if count == 20:
                break
            status = self.check_emp_present_or_absent()
            if status:
                emp_hrs = 0
                rate_per_hrs = 20
                if self.work_type == 1:
                    emp_hrs = 8
                elif self.work_type == 2:
                    emp_hrs = 4
                else:
                    emp_hrs = 0
                emp_wage += emp_hrs * rate_per_hrs
            else:
                print("employee is absent at day:"+str(count))
        print("total monthly wage "+str(emp_wage))


def main():
    print("welcome to employee wage computation")
    work_type_input = input("enter '1' if full_time else '2' for part_time ")
    employee = Employee("Andra", 1, "IT", int(work_type_input), 1)
    employee.calculate_monthly_wage()


if __name__ == '__main__':
    main()