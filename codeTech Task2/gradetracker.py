class Student:
  def __init__(self, name):
    self.name = name
    self.grades = {}

  def add_grade(self, subject, grade):
    self.grades[subject] = grade

  def calculate_average(self):
    return sum(self.grades.values()) / len(self.grades)

  def get_letter_grade(self, average):
    if average >= 90:
      return "A"
    elif average >= 80:
      return "B"
    elif average >= 70:
      return "C"
    elif average >= 60:
      return "D"
    else:
      return "F"

  def get_gpa(self, average):
    if average >= 90:
      return 4.0
    elif average >= 80:
      return 3.0
    elif average >= 70:
      return 2.0
    elif average >= 60:
      return 1.0
    else:
      return 0.0

  def display_grades(self):
    print(f"Student: {self.name}")
    print("Grades:")
    for subject, grade in self.grades.items():
      print(f"  {subject}: {grade}")
    average = self.calculate_average()
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {self.get_letter_grade(average)}")
    print(f"GPA: {self.get_gpa(average):.1f}")

def main():
  student_name = input("Enter the student's name: ")
  student = Student(student_name)

  while True:
    print("\nOptions:")
    print("1. Add grade")
    print("2. Display grades")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
      subject = input("Enter the subject: ")
      grade = float(input("Enter the grade: "))
      student.add_grade(subject, grade)
    elif choice == "2":
      student.display_grades()
    elif choice == "3":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()