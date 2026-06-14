from storage import load_data, save_data

PLAN_FILE = "study_plan.json"

def add_study_session():
    plan = load_data(PLAN_FILE, [])
    subject = input("Subject: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time (e.g., 7:00 PM): ").strip()
    goal = input("Study goal: ").strip()

    if not subject or not goal:
        print("Subject and goal are required.")
        return

    session = {
        "id": len(plan) + 1,
        "subject": subject,
        "date": date,
        "time": time,
        "goal": goal
    }
    plan.append(session)
    save_data(PLAN_FILE, plan)
    print("Study session added.")

def view_study_plan():
    plan = load_data(PLAN_FILE, [])
    if not plan:
        print("No study sessions planned.")
        return

    print("\n--- Study Plan ---")
    for session in plan:
        print(f'{session["id"]}. {session["subject"]} | {session["date"]} {session["time"]} | Goal: {session["goal"]}')

def delete_study_session():
    plan = load_data(PLAN_FILE, [])
    view_study_plan()
    try:
        session_id = int(input("Enter session ID to delete: "))
        plan = [session for session in plan if session["id"] != session_id]
        for index, session in enumerate(plan, start=1):
            session["id"] = index
        save_data(PLAN_FILE, plan)
        print("Study session deleted.")
    except ValueError:
        print("Invalid session ID.")

def planner_menu():
    while True:
        print("\n--- Study Planner ---")
        print("1. Add Study Session")
        print("2. View Study Plan")
        print("3. Delete Study Session")
        print("4. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_study_session()
        elif choice == "2":
            view_study_plan()
        elif choice == "3":
            delete_study_session()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
