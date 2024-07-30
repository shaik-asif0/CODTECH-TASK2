# CODTECH-TASK2
<h2>Intern</h2>
<b>Name:</b> SHAIK ASIF<br>
<b>Collage:</b> NRI Institute of technology<BR>
<b>Roll No:</b>22KP1A44A9<BR>
<b>Company:</b>CODTECH IT SOLUTIONS<BR>
<b>ID:</b>CT4PP3591<BR>
<b>Domain:</b>PYTHON PROGRAMMING<BR>
<b>Duration:</b> JULY TO AUGUST 2024<BR>
<b>Mentor:</b>SRAVANI GOUNI<BR>

<h2>STUDENT GRADE TRACKER</h2>
<b>Sample Code:</b><br><br>
<pre>
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

</pre><br>
# OutPut
![image](https://github.com/user-attachments/assets/ecfae6e7-593f-4bbf-9f5f-32c416eaadf1)


<br>
<h2>Project Over View</h2>

1. **Class Definition (`Student`):**
   - The `Student` class represents a student and has the following methods:
     - `__init__(self, name)`: Initializes a student object with a given name and an empty dictionary for grades.
     - `add_grade(self, subject, grade)`: Adds a grade for a specific subject.
     - `calculate_average(self)`: Calculates the average grade across all subjects.
     - `get_letter_grade(self, average)`: Converts the average grade to a letter grade (A, B, C, D, or F).
     - `get_gpa(self, average)`: Calculates the GPA based on the average grade.
     - `display_grades(self)`: Displays the student's name, individual subject grades, average, letter grade, and GPA.

2. **Main Function (`main()`):**
   - The `main()` function is the entry point of the program.
   - It prompts the user for the student's name and creates a `Student` object.
   - Inside a loop, it offers three options:
     - **Add Grade:** Allows the user to input a subject and grade, which are added to the student's record.
     - **Display Grades:** Shows the student's name, individual subject grades, average, letter grade, and GPA.
     - **Quit:** Exits the program.
   - The loop continues until the user chooses to quit.

3. **Usage:**
   - Run this program in a Python environment (e.g., command line, Jupyter Notebook, or an IDE).
   - Follow the prompts to add grades and display information.
# CODTECH-TASK2
