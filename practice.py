
class TodoManager:
    def __init__(self):
        self.todos=[]
    def add_todo(self, task: str,status:bool):
        todo_id=len(self.todos)+1
        self.todos.append({"id": todo_id, "task": task, "done": status})

    def get_all(self):
        return self.todos
    
    def get_item(self,task:str):
        values = ""
        for todo in self.todos:
            if todo["task"] == task:
                values = todo
                break
        return values
        

manager = TodoManager()
manager.add_todo("Walk dog",True)
manager.add_todo("get milk",False)
print("*************")
print(manager.get_all())



todos=[]
todos.append({"id": 1, "task": "Buy milk", "done":False})
todos.append({"id": 2, "task": "Learn Python", "done":True})
print(todos)


for todo in todos:
    status="Done" if todo["done"] else "Pending"
    print(f"ID: {todo['id']}, Task: {todo['task']}, Status: {status}")
