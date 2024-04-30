class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if not self.tasks:
            print("Keine Aufgaben vorhanden.")
        else:
            print("Offene Aufgaben:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Erledigt" if task.completed else "Offen"
                print(f"{idx}. {task.description} - Fällig am: {task.due_date} - Status: {status}")

    def mark_task_completed(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1].mark_as_completed()
            print("Aufgabe als erledigt markiert.")
        else:
            print("Ungültiger Index.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.due_date},{task.completed}\n")

    def load_tasks(self, filename):
        self.tasks = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    description, due_date, completed = line.strip().split(',')
                    self.tasks.append(Task(description, due_date, completed=='True'))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.load_tasks('tasks.txt')

    while True:
        print("\n1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Beenden")

        choice = input("Bitte wähle eine Option: ")

        if choice == "1":
            description = input("Beschreibung der Aufgabe: ")
            due_date = input("Fälligkeitsdatum (Format: YYYY-MM-DD): ")
            task = Task(description, due_date)
            task_manager.add_task(task)
            print("Aufgabe hinzugefügt.")
        elif choice == "2":
            task_manager.display_tasks()
        elif choice == "3":
            task_idx = int(input("Index der abgeschlossenen Aufgabe eingeben: "))
            task_manager.mark_task_completed(task_idx)
        elif choice == "4":
            task_manager.save_tasks('tasks.txt')
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine der verfügbaren Optionen.")
