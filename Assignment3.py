# Task class represents a single task
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.status = "incomplete"  # Initial status is incomplete

    # Method to mark task as complete
    def mark_complete(self):
        self.status = "complete"

    # Overriding __str__ method to display task details
    def __str__(self):
        return f"Task: {self.title} - Status: {self.status}"

# PriorityTask class that inherits from Task and adds a priority attribute
class PriorityTask(Task):
    def __init__(self, title, description="", priority="low"):
        super().__init__(title, description)  # Inheritance
        self.priority = priority

    # Overriding __str__ method to include priority
    def __str__(self):
        return f"Priority Task: {self.title} - Status: {self.status} - Priority: {self.priority}"

# TaskList class represents a collection of tasks
class TaskList:
    def __init__(self):
        self.tasks = []  # Encapsulation: tasks list is private

    # Method overloading to add tasks with or without description
    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    # Method to add a priority task
    def add_priority_task(self, title, description="", priority="low"):
        task = PriorityTask(title, description, priority)
        self.tasks.append(task)

    # Method to remove a task by title
    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    # Method to list all tasks
    def list_tasks(self):
        print("\nTasks:")
        for task in self.tasks:
            print(task)

    # Method to find a task by title
    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    # Method to mark a task as complete by title
    def mark_task_complete(self, title):
        task = self.find_task(title)
        if task:
            task.mark_complete()
        else:
            print(f"Task with title '{title}' not found.")

    # Method to find a priority task by title
    def find_priority_task(self, title):
        for task in self.tasks:
            if isinstance(task, PriorityTask) and task.title == title:  # Polymorphism
                return task
        return None

# Demonstration of the Task List Application
def main():
    task_list = TaskList()

    # Adding tasks
    task_list.add_task("Do homework")
    task_list.add_task("Go to the gym", "Cardio workout")
    task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")

    # Listing tasks
    task_list.list_tasks()

    # Marking a task as complete
    task_list.mark_task_complete("Go to the gym")

    # Finding and printing specific tasks
    print("\nSpecific Tasks:")
    print(task_list.find_task("Do homework"))
    print(task_list.find_priority_task("Buy groceries"))

if __name__ == "__main__":
    main()
