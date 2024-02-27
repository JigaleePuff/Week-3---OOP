class student():
    def __init__(self, name, gender, student_ID, subject):
        self.name = name
        self.gender = gender
        self.student_ID = student_ID
        self.subject = subject

    def show_details(self):
        print(f"Student name: {self.name}\nGender: {self.gender}") #Seperate line "\n" is used to make the output in new lines
        print(f"Student ID: {self.student_ID} - Student Subject: {self.subject}")

    def submission(self, score):
        self.grade = score
        print(f"Grade Book has been updated - Current Grade: {self.grade}")

    def attendance(self, attendance):
        self.register = attendance 
        print(f"Attendance Percentage: {attendance}%")

# Creating an instance of the student class with appropriate arguments
carol = student("Carol", "Female", "UWI12345", "Quantum Computing")

# Calling the show_details method to display Carol's details
carol.show_details()

# Calling the submission method to update Carol's grade
carol.submission(100)

# Calling the attendance method to update Carol's attendance
carol.attendance(100)
