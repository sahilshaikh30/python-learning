# ---------------- STUDENT PERFORMANCE ANALYZER ----------------

# Create a Student class to manage student details and marks
class Student:

  # Class variable shared by all Student objects
  school = "Bright Academy"

  # Constructor: runs automatically when a Student object is created
  def __init__(self, name, math, science, english):

    # Store the student's name and subject marks
    self.name = name
    self.math = math
    self.science = science 
    self.english = english

  # ---------------- CALCULATE TOTAL MARKS ----------------

  # Add marks from all three subjects
  def calculate_total(self):
    total_marks = (self.math + self.science + self.english)
    return total_marks

  # ---------------- CALCULATE AVERAGE MARKS ----------------

  # Calculate average by dividing total marks by 3 subjects
  def calculate_avg(self):
    avg = self.calculate_total() / 3
    return avg

  # ---------------- CHECK PASS OR FAIL ----------------

  # Check whether the student's average is at least 40
  def is_passed(self):
    if self.calculate_avg() >= 40:
      if_passed = True
    else:
      if_passed = False
    return if_passed


  # ---------------- GENERATE STUDENT REPORT ----------------

  # Return a formatted report containing student performance
  def get_report(self):
    return f"""
Name: {self.name}
School: {self.school}
Total Marks: {self.calculate_total()}
Average Marks: {self.calculate_avg()}
Passed: {self.is_passed()}
"""


# Create a Student object with the student's name and subject marks
data = Student("Rahul",75,82,68)

# Call get_report() and display the complete report
print(data.get_report())