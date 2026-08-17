from flask import Flask, render_template, request
from attendance import calculate_attendance, get_status

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        employee_name = request.form["employee_name"]
        days_present = int(request.form["days_present"])
        total_days = int(request.form["total_days"])

        if days_present > total_days:
            error = "Days present cannot be greater than total working days."
        else:
            attendance_percentage = calculate_attendance(
                days_present, total_days
            )
            status = get_status(attendance_percentage)

            result = {
                "employee_name": employee_name,
                "days_present": days_present,
                "total_days": total_days,
                "attendance": attendance_percentage,
                "status": status,
            }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)