from attendance import calculate_attendance, get_status
print("Employee Attendance Tracker")
print("---------------------------")

employee_name = input("Enter employee name: ")
days_present = int(input("Enter days present: "))
total_days = int(input("Enter total working days: "))

if days_present > total_days:
    print("Error: Days present cannot be greater than total working days.")
else:
    attendance_percentage = calculate_attendance(days_present, total_days)
    status = get_status(attendance_percentage)
    

    print()
    print("Employee:", employee_name)
    print("Days Present:", days_present)
    print("Total Days:", total_days)
    print("Attendance:", attendance_percentage, "%")
    print("Status:", status)
    print("Thank you for using the Employee Attendance Tracker!")
    print("See you next time")

