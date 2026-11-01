
# ---------------- USER INPUT ----------------

# Get the user's sleeping hours
sleeping_hours = float(input("Enter your Sleeping hours: "))

# Get the user's energy level out of 10
energy_level = int(input("Enter your energy level(out of 10): "))

# Get the available focus time in minutes
focus_time = int(input("Enter your available focus time(in mins): "))


# ---------------- SLEEP SCORE ----------------

# Give maximum 40 points if sleeping hours are 8 or more
if (sleeping_hours >= 8):
    sleep_score = 40

# Otherwise, calculate 5 points for every hour of sleep
elif (sleeping_hours < 8):
    sleep_score = 5 * sleeping_hours


# ---------------- ENERGY SCORE ----------------

# Calculate energy score by multiplying energy level by 3.5
energy_score = 3.5 * energy_level


# ---------------- FOCUS SCORE ----------------

# Give maximum 25 points if available focus time is 120 minutes or more
if (focus_time >= 120):
    focus_score = 25

# Otherwise, calculate the focus score based on available minutes
elif (focus_time < 120):
    focus_score = focus_time / 4.8


# ---------------- TOTAL SCORE ----------------

# Add all three scores to calculate the total readiness score
total_score = sleep_score + energy_score + focus_score


# ---------------- READINESS LEVEL ----------------

# Assign readiness level based on the total score
if (total_score >= 80):
    readiness = "Highly Ready"

# Assign moderate readiness if score is between 60 and 80
elif (total_score >= 60 and total_score < 80):
    readiness = "Moderately Ready"

# Assign recovery status if score is below 60
else:
    readiness = "Needs Recovery"


# ---------------- FINAL REPORT ----------------

# Display all inputs, individual scores and final readiness level
print(f'''
========================
Sleeping hours: {sleeping_hours}
Energy level: {energy_level}
Available focus time: {focus_time}

Sleeping score: {sleep_score}
Energy score: {energy_score}
Focus score: {focus_score}

Total score: {total_score}
Readiness level: {readiness}
========================
''')
