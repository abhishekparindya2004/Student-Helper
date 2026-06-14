def marks_calculator():
    print("\n--- Marks Calculator ---")
    try:
        count = int(input("How many subjects/modules? "))
        if count <= 0:
            print("Subject count must be positive.")
            return

        total = 0
        results = []
        for i in range(count):
            subject = input(f"Subject {i + 1} name: ").strip()
            mark = float(input(f"Marks for {subject}: "))
            total += mark
            results.append((subject, mark, grade_from_mark(mark)))

        average = total / count
        print("\n--- Results ---")
        for subject, mark, grade in results:
            print(f"{subject}: {mark:.2f} - {grade}")
        print(f"Average: {average:.2f}")
        print(f"Overall Grade: {grade_from_mark(average)}")
    except ValueError:
        print("Please enter valid numbers.")

def grade_from_mark(mark):
    if mark >= 85:
        return "A+"
    if mark >= 75:
        return "A"
    if mark >= 65:
        return "B"
    if mark >= 55:
        return "C"
    if mark >= 40:
        return "S / Pass"
    return "F / Fail"

def gpa_calculator():
    print("\n--- GPA Calculator ---")
    grade_points = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D": 1.0,
        "F": 0.0
    }

    try:
        count = int(input("How many modules? "))
        total_points = 0
        total_credits = 0

        for i in range(count):
            module = input(f"Module {i + 1}: ").strip()
            grade = input(f"Grade for {module} (A+, A, A-, B+, B, B-, C+, C, C-, D, F): ").upper().strip()
            credits = float(input(f"Credits for {module}: "))

            if grade not in grade_points:
                print("Invalid grade. Try again.")
                return

            total_points += grade_points[grade] * credits
            total_credits += credits

        if total_credits == 0:
            print("Credits cannot be zero.")
            return

        gpa = total_points / total_credits
        print(f"Your GPA is: {gpa:.2f}")
    except ValueError:
        print("Invalid input.")

def gpa_menu():
    while True:
        print("\n--- GPA & Marks ---")
        print("1. Marks Calculator")
        print("2. GPA Calculator")
        print("3. Back")
        choice = input("Choose: ")

        if choice == "1":
            marks_calculator()
        elif choice == "2":
            gpa_calculator()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
