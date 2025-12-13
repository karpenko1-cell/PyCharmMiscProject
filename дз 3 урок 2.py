class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = False

    def complete(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано")

    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Завдання '{task.title}' видалено")

    def show(self):
        if self.tasks == []:
            print("Завдань немає")
        else:
            for task in self.tasks:
                status = "Виконано" if task.done else "Не виконано"
                print(task.title, "-", status, "| дедлайн:", task.deadline)



t1 = Task("Домашка з Python", "Зробити класи", "15.12")
t2 = Task("Англійська", "Вивчити слова", "14.12")

manager = TaskManager()
manager.add(t1)
manager.add(t2)
t1.complete()
manager.show()