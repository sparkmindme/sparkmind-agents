class PlannerAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task added: {task}"

    def get_tasks(self):
        return self.tasks
