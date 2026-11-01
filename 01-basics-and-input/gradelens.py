
# ---------------- STUDENT INPUT ----------------

# Get the student's name
name = input("Enter name: ")

# Get marks in each subject (out of 100)
math_marks = int(input("Enter Maths marks(out of 100): "))
science_marks = int(input("Enter Science marks(out of 100): "))
english_marks = int(input("Enter English marks(out of 100): "))


# ---------------- TOTAL MARKS ----------------

# Add marks from all three subjects
total_marks = math_marks + science_marks + english_marks

# Calculate overall percentage (maximum marks = 300)
percentage = (total_marks / 300) * 100


# ---------------- PASS OR FAIL ----------------

# Student fails if they score below 35 in any subject
if (math_marks < 35 or science_marks < 35 or english_marks < 35):
    result = "Fail"
else:
    result = "Pass"


# ---------------- GRADE CALCULATION ----------------

# Assign grade based on the overall percentage
if percentage >= 90:
    grade = "A"

# Grade B: 80% to below 90%
elif percentage >= 80 and percentage < 90:
    grade = "B"

# Grade C: 70% to below 80%
elif percentage >= 70 and percentage < 80:
    grade = "C"

# Grade D: 60% to below 70%
elif percentage >= 60 and percentage < 70:
    grade = "D"

# Grade E: Below 60%
elif percentage < 60:
    grade = "E"


# ---------------- FINAL REPORT ----------------

# Display the student's marks, percentage, result and grade
print(f'''
GradeLens
========================
Name: {name}

Maths: {math_marks}
Science: {science_marks}
English: {english_marks}

Total marks: {total_marks}
Percentage: {percentage:.2f}
Result: {result}
Grade: {grade}
========================
''')
