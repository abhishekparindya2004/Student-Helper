from storage import load_data, save_data
from tasks import task_menu
from notes import notes_menu
from gpa import gpa_menu
from quiz import quiz_menu
from planner import planner_menu
from dashboard import show_dashboard

PROFILE_FILE = "profile.json"

def setup_profile():
    profile = load_data(PROFILE_FILE, {})
    if profile.get("name"):
        return profile

    print("Welcome to Student Helper!")
    name = input("Enter your name: ").strip()
    course = input("Enter your course/degree: ").strip()
    university = input("Enter your school/university: ").strip()

    profile = {
        "name": name or "Student",
        "course": course or "Not set",
        "university": university or "Not set"
    }
    save_data(PROFILE_FILE, profile)
    return profile

def view_profile():
    profile = load_data(PROFILE_FILE, {})
    print("\n--- Student Profile ---")
    print(f"Name: {profile.get('name', 'Student')}")
    print(f"Course: {profile.get('course', 'Not set')}")
    print(f"University: {profile.get('university', 'Not set')}")

def edit_profile():
    profile = load_data(PROFILE_FILE, {})
    name = input(f"Name [{profile.get('name', '')}]: ").strip()
    course = input(f"Course [{profile.get('course', '')}]: ").strip()
    university = input(f"University [{profile.get('university', '')}]: ").strip()

    if name:
        profile["name"] = name
    if course:
        profile["course"] = course
    if university:
        profile["university"] = university

    save_data(PROFILE_FILE, profile)
    print("Profile updated.")

def main_menu():
    profile = setup_profile()

    while True:
        print(f"\nHello, {profile.get('name', 'Student')}!")
        print("========== Student Helper ==========")
        print("1. Dashboard")
        print("2. Task Manager")
        print("3. Notes Manager")
        print("4. GPA & Marks Calculator")
        print("5. Quiz Practice")
        print("6. Study Planner")
        print("7. View Profile")
        print("8. Edit Profile")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_dashboard()
        elif choice == "2":
            task_menu()
        elif choice == "3":
            notes_menu()
        elif choice == "4":
            gpa_menu()
        elif choice == "5":
            quiz_menu()
        elif choice == "6":
            planner_menu()
        elif choice == "7":
            view_profile()
        elif choice == "8":
            edit_profile()
            profile = load_data(PROFILE_FILE, {})
        elif choice == "9":
            print("Goodbye. Study well!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
