import pandas as pd
import random
print ("TIMETABLE GENERATOR\n")
subjects_input = input ("Enter subjects (comma separated): ")
days_input = input ("Enter days (comma separated): ")
periods_per_day = int(input("Enter number of periods per day: "))
subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]
days = [d.strip() for d in days_input.split(",") if d.strip()]
if len(subjects) == 0 or len(days) == 0 or periods_per_day <= 0:
  print("Invalid input. Please try again.")
else:
  print("Invalid input. Please try again.")

  timetable = {}

for day in days:
  timetable[day] = random.choices(subjects, k=periods_per_day)
  df = pd.DataFrame(timetable)
df.index = [f"Period {i+1}" for i in range(periods_per_day)]
print("Timetable Generated Successfully\n")
display(df)
df.to_csv("timetable.csv")
print("\nTimetable saved as timetable.csv")
