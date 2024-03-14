import json

class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = {"id": task_id, "title": title, "description": description, "status": "Pending"}
        self.tasks.append(task)
        self.save_tasks_to_file()
        print(f"Task added successfully with ID: {task_id}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                self.save_tasks_to_file()
                print(f"Task with ID {task_id} marked as completed")
                return
        print(f"Task with ID {task_id} not found")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return
        for task in self.tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")

    def save_tasks_to_file(self):
        with open("data/tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

def load_tasks_from_file():
    try:
        with open("data/tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks_from_file()

    # Contoh penggunaan TaskManager
    task_manager.add_task("Task 3", "Description for Task 3")
    task_manager.complete_task(1)
    task_manager.show_tasks()

if __name__ == "__main__":
    main()
