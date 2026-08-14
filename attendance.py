def calculate_attendance(days_present, total_days):
    return round((days_present / total_days) * 100, 2)


def get_status(attendance_percentage):
    if attendance_percentage >= 75:
        return "Good"
    else:
        return "Needs Improvement"