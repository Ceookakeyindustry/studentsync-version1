students = []

while True:

    choice = int(input("""
=========================
 STUDENT GRADE MANAGER
=========================

1. Add Student
2. View Students
3. Search Student
4. Edit Student
5. Delete Student
6. Exit

Choose an option: """))

    if choice == 1:

        print("\nPlease enter student details:\n")

        name = input("Enter Name of Student: ")
        roll_number = int(input("Enter Roll Number of Student: "))
        student_class = int(input("Enter Class of Student: "))
        maths_marks = float(input("Enter Maths Marks of Student: "))
        science_marks = float(input("Enter Science Marks of Student: "))
        english_marks = float(input("Enter English Marks of Student: "))

        average = (maths_marks + science_marks + english_marks) / 3

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        student = {
            "name": name,
            "roll_number": roll_number,
            "student_class": student_class,
            "maths_marks": maths_marks,
            "science_marks": science_marks,
            "english_marks": english_marks,
            "average": average,
            "grade": grade
        }

        students.append(student)

        print("\nStudent Added Successfully!\n")

    elif choice == 2:

        print("\n===== STUDENTS =====")

        if len(students) == 0:
            print("No students found.")

        else:

            for student in students:

                print("-------------------------")
                print(f"Name: {student['name']}")
                print(f"Roll Number: {student['roll_number']}")
                print(f"Class: {student['student_class']}")
                print(f"Maths Marks: {student['maths_marks']}")
                print(f"Science Marks: {student['science_marks']}")
                print(f"English Marks: {student['english_marks']}")
                print(f"Average: {student['average']:.2f}")
                print(f"Grade: {student['grade']}")
                print("-------------------------")

    elif choice == 3:
        search_roll_number = int(input("Enter Roll Number of Student to Search: "))
        for student in students:
            if student['roll_number'] == search_roll_number:
                print("-------------------------")
                print("STUDENT FOUND!")
                print(f"Name: {student['name']}")
                print(f"Roll Number: {student['roll_number']}")
                print(f"Class: {student['student_class']}")
                print(f"Maths Marks: {student['maths_marks']}")
                print(f"Science Marks: {student['science_marks']}")
                print(f"English Marks: {student['english_marks']}")
                print(f"Average: {student['average']:.2f}")
                print(f"Grade: {student['grade']}")
                print("-------------------------")
                break
        else:
            print("Student not found.")

    elif choice == 4:
        edit_roll_number = int(input("Enter Roll Number of Student to Edit: "))
        for student in students:
            if student['roll_number'] == edit_roll_number:
                print("-------------------------")
                print("STUDENT FOUND!")
                print(f"Name: {student['name']}")
                print(f"Roll Number: {student['roll_number']}")
                print(f"Class: {student['student_class']}")
                print(f"Maths Marks: {student['maths_marks']}")
                print(f"Science Marks: {student['science_marks']}")
                print(f"English Marks: {student['english_marks']}")
                print(f"Average: {student['average']:.2f}")
                print(f"Grade: {student['grade']}")
                print("-------------------------")

                # Edit student details
                student['name'] = input("Enter New Name of Student: ")
                student['student_class'] = int(input("Enter New Class of Student: "))
                student['maths_marks'] = float(input("Enter New Maths Marks of Student: "))
                student['science_marks'] = float(input("Enter New Science Marks of Student: "))
                student['english_marks'] = float(input("Enter New English Marks of Student: "))

                # Recalculate average and grade
                average = (student['maths_marks'] + student['science_marks'] + student['english_marks']) / 3
                student['average'] = average

                if average >= 90:
                    student['grade'] = "A+"
                elif average >= 80:
                    student['grade'] = "A"
                elif average >= 70:
                    student['grade'] = "B"
                elif average >= 60:
                    student['grade'] = "C"
                else:
                    student['grade'] = "D"

                print("\nStudent Details Updated Successfully!\n")
                break
        else:
            print("Student not found.")
    elif choice == 5:
        delete_roll_number = int(input("Enter Roll Number of Student to Delete: "))
        for student in students:
            if student['roll_number'] == delete_roll_number:
                students.remove(student)
                print("\nStudent Deleted Successfully!\n")
        else:
            print("Student not found.")
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Wrong Command!")
