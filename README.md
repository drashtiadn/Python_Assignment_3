# Python_Assignment_3
Assignment: Python OOP Mini Project

Instructions:

Write your solutions in Python.
Follow good programming practices, including proper class design and comments.
Build a Python project that incorporates the following OOP concepts: classes, objects, methods, method overloading, method overriding, inheritance, encapsulation, and polymorphism.
Provide evidence-based documentation that explains how you've implemented these concepts in your project.
Project Description: Task List Application

You are tasked with creating a Task List Application. This application should allow users to manage a list of tasks. Each task has a title, a description, and a status (e.g., incomplete or complete).

OOP Implementation:

Create a Task class that represents a single task. It should have the following attributes: title, description, and status.
Implement a constructor to initialize the task with a title, description, and an initial status of "incomplete."
Implement a method in the Task class to mark a task as complete.
Create a TaskList class that represents a collection of tasks.
Implement methods in the TaskList class to add tasks, remove tasks, list all tasks, and find tasks by title.
Use method overloading to allow different ways of adding tasks (e.g., with or without a description).
Use method overriding to customize the to_s method in the Task class to display task details in a user-friendly format.
Implement inheritance by creating a PriorityTask class that inherits from Task. Priority tasks have an additional priority attribute (e.g., low, medium, high).
In your submission, provide documentation that explains how you've applied each of the OOP concepts mentioned above. Include comments in your code that highlight the use of methods, classes, method overloading, method overriding, inheritance, encapsulation, and polymorphism.

# Sample usage of your Task List Application

task_list = TaskList.new

task_list.add_task("Do homework")

task_list.add_task("Go to the gym", "Cardio workout")

task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")

task_list.list_tasks

task_list.mark_task_complete("Go to the gym")

puts task_list.find_task("Do homework")

puts task_list.find_priority_task("Buy groceries")

# Output:

# Tasks:

# Task: Do homework - Status: incomplete

# Task: Go to the gym - Status: complete

#

# Task: Do homework - Status: incomplete

# Priority Task: Buy groceries - Status: incomplete - Priority: high

Evaluation Criteria

OOP Concept Implementation: 18 Marks

Evaluates the effective use of OOP concepts like classes, objects, and various methods. Also assesses understanding through documentation and comments.
Functionality and Correctness: 15 Marks

Focuses on the accurate implementation of functionalities such as task operations and status handling.
Code Quality and Standards: 10 Marks

Reviews the code's structure, readability, naming conventions, and adherence to best practices.
User Interface and Interaction: 5 Marks

Assesses the clarity and user-friendliness of the interface and the effectiveness of user input handling.
Documentation and Presentation: 2 Marks

Evaluates the clarity of documentation and the professional presentation of the code.
