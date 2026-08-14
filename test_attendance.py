import unittest
from attendance import calculate_attendance, get_status


class TestAttendance(unittest.TestCase):

    def test_calculate_attendance(self):
        result = calculate_attendance(12, 15)
        self.assertEqual(result, 80.0)

    def test_get_status(self):
        result = get_status(80)
        self.assertEqual(result, "Good")


if __name__ == "__main__":
    unittest.main()