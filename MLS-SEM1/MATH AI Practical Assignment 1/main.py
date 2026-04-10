def read_file_to_dict(filename):
    student_dict = {}
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                student_dict[key.strip()] = [float(value.strip())]
    return student_dict

def add_student(student_dict, name, grade):
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(grade)


def calculate_average(student_dict):
    average = 0
    count = 0
    for grades in student_dict.values():
        average += sum(grades)
        count += 1
    return average/count


def print_above_average_students(student_dict, averages):
    above_average = {}
    for name, grades in student_dict.items():
        if grades[0] > averages:
            above_average[name] = grades[0]
    return above_average


# Main program
if __name__ == "__main__":
    filename = "students.txt"
    students = read_file_to_dict(filename)

    while True:
        print("\nOptions:")
        print("1. Add new student data")
        print("2. Calculate average grade")
        print("3. Print students who scored above average")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students, input("Enter student name: "), float(input("Enter grade: ")))

        elif choice == "2":
            averages = calculate_average(students)
            print("Averages:", averages)

        elif choice == "3":
            above_avg = print_above_average_students(students, calculate_average(students))
            print("Above average students:", above_avg)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")