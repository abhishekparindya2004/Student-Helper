from storage import load_data, save_data

NOTE_FILE = "notes.json"

def add_note():
    notes = load_data(NOTE_FILE, [])
    subject = input("Subject: ").strip()
    title = input("Note title: ").strip()
    content = input("Note content: ").strip()

    if not title or not content:
        print("Title and content are required.")
        return

    note = {
        "id": len(notes) + 1,
        "subject": subject,
        "title": title,
        "content": content
    }
    notes.append(note)
    save_data(NOTE_FILE, notes)
    print("Note saved.")

def view_notes():
    notes = load_data(NOTE_FILE, [])
    if not notes:
        print("No notes found.")
        return

    print("\n--- Notes ---")
    for note in notes:
        print(f'\n{note["id"]}. {note["title"]} ({note["subject"]})')
        print(note["content"])

def search_notes():
    notes = load_data(NOTE_FILE, [])
    keyword = input("Search keyword: ").lower().strip()
    found = [note for note in notes if keyword in note["title"].lower() or keyword in note["content"].lower() or keyword in note["subject"].lower()]

    if not found:
        print("No matching notes found.")
        return

    for note in found:
        print(f'\n{note["id"]}. {note["title"]} ({note["subject"]})')
        print(note["content"])

def delete_note():
    notes = load_data(NOTE_FILE, [])
    view_notes()
    try:
        note_id = int(input("Enter note ID to delete: "))
        notes = [note for note in notes if note["id"] != note_id]
        for index, note in enumerate(notes, start=1):
            note["id"] = index
        save_data(NOTE_FILE, notes)
        print("Note deleted.")
    except ValueError:
        print("Invalid note ID.")

def notes_menu():
    while True:
        print("\n--- Notes Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
