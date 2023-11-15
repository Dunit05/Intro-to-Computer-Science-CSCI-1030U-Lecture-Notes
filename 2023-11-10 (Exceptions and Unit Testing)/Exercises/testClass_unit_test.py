import unittest
from testClass import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(3.5, "John")
        self.assertEqual(
            self.student.gpa, 3.5, msg="GPA is not set properly, should be 3.5"
        )
        self.assertEqual(
            self.student.name, "John", msg="Name is not set properly, should be John"
        )
        self.assertEqual(self.student.marks, [], msg="Marks should be an empty list")
        self.student.set_mark("Math", 90)
        self.student.set_mark("English", 80)
        self.student.set_mark("Science", 70)

    def test_get_average(self):
        self.assertEqual(self.student.get_average(), 80)

    def test_set_mark(self):
        self.student.set_mark("History", 60)
        self.assertEqual(self.student.get_average(), 75)


unittest.main()
