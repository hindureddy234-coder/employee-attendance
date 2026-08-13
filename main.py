print("Employee Attendance Tracker")
print("Welcome!")
employee_name = "Hindu"
days_present = 18
total_days = 20

attendance_percentage = (days_present / total_days) * 100

print("Employee Attendance Tracker")
print("---------------------------")
print("Employee:", employee_name)
print("Days Present:", days_present)
print("Total Days:", total_days)
print("Attendance:", attendance_percentage, "%")
print("Employee Attendance Tracker")
print("---------------------------")

employee_name = input("Enter employee name: ")
days_present = int(input("Enter days present: "))
total_days = int(input("Enter total working days: "))

attendance_percentage = (days_present / total_days) * 100

if attendance_percentage >= 75:
    status = "Good"
else:
    status = "Needs Improvement"

print()
print("Employee:", employee_name)
print("Days Present:", days_present)
print("Total Days:", total_days)
print("Attendance:", attendance_percentage, "%")
print("Status:", status)
print("Thank you for using the Employee Attendance Tracker!")
