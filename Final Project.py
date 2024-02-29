import json

def load_attendance():
    try:
        with open("attendance.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_attendance(attendance):
    with open("attendance.json", "w") as file:
        json.dump(attendance, file)

def mark_attendance(student_name, father_name, present_mark='X', absent_mark='-'):
    attendance = load_attendance()
    student_name_lower = student_name.lower()
    father_name_lower = father_name.lower()
    if student_name_lower in attendance:
        print(f"{student_name} (Father: {attendance[student_name_lower]['Father']}) has already been marked.")
    else:
        status = input(f"Mark {student_name} present (P) or absent (A): ").upper()
        if status == 'P':
            attendance[student_name_lower] = {"Father": father_name_lower, "Status": "Present", "Mark": present_mark}
            save_attendance(attendance)
            print(f"{student_name} (Father: {father_name}) has been marked present.")
        elif status == 'A':
            attendance[student_name_lower] = {"Father": father_name_lower, "Status": "Absent", "Mark": absent_mark}
            save_attendance(attendance)
            print(f"{student_name} (Father: {father_name}) has been marked absent.")
        else:
            print("Invalid input. Please enter 'P' for present or 'A' for absent.")

def view_attendance():
    attendance = load_attendance()
    if not attendance:
        print("No attendance data available.")
    else:
        print("Attendance:")
        for student, info in attendance.items():
            print(f"Name: {student} (Father: {info['Father']}): {info['Status']} ({info.get('Mark', '')})")

def main():
    while True:
        print("\n1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            student_name = input("Enter student's name: ")
            father_name = input("Enter father's name: ")
            mark_attendance(student_name, father_name)
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
