
# Employee class: Blueprint for creating employee objects
class Employee:

    # Class variable: Company name shared by all employees
    company = "TechSolutions"

    # Constructor: Initializes employee details when an object is created
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    # Calculates the employee's total salary (base salary + bonus)
    def calculate_total_salary(self):
        total_salary = self.salary + self.bonus
        return total_salary

    # Checks whether the employee qualifies as a high earner
    def is_high_earner(self):

        # Employee is a high earner if total salary is ₹50,000 or more
        if self.calculate_total_salary() >= 50000:
            salary_good = True
        else:
            salary_good = False

        return salary_good

    # Generates a report containing all employee details
    def get_report(self):
        return f"""
Company: {self.company}
Employee: {self.name}
Base Salary: {self.salary}
Bonus: {self.bonus}
Total Salary: {self.calculate_total_salary()}
High Earner: {self.is_high_earner()}
"""


# Create an Employee object with name, salary and bonus
data = Employee("Rahul", 45000, 8000)

# Display the employee report
print(data.get_report())
