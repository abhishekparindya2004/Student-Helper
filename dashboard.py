from storage import load_data

def show_dashboard():
    tasks = load_data("tasks.json", [])
    notes = load_data("notes.json", [])
    quizzes = load_data("quiz_history.json", [])
    plan = load_data("study_plan.json", [])

    completed_tasks = len([task for task in tasks if task.get("completed")])
    pending_tasks = len(tasks) - completed_tasks

    print("\n========== Student Dashboard ==========")
    print(f"Total Tasks: {len(tasks)}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Saved Notes: {len(notes)}")
    print(f"Planned Study Sessions: {len(plan)}")

    if quizzes:
        best_score = max(item["percentage"] for item in quizzes)
        latest = quizzes[-1]
        print(f"Quiz Attempts: {len(quizzes)}")
        print(f"Latest Quiz Score: {latest['percentage']}%")
        print(f"Best Quiz Score: {best_score}%")
    else:
        print("Quiz Attempts: 0")

    print("======================================")
