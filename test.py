import practice

manager222 = practice.TodoManager()
manager222.add_todo("open dooor",False)
manager222.add_todo("Walk dog",True)
manager222.add_todo("get milk",False)
print(manager222.get_all())
print(manager222.get_item("open door"))



todos=[]
todos.append({"id": 1, "task": "Buy milk", "done":False})
todos.append({"id": 2, "task": "Learn Python", "done":True})
print(todos)


for todo in todos:
    status="Done" if todo["done"] else "Pending"
    print(f"ID: {todo['id']}, Task: {todo['task']}, Status: {status}")



   
manager = TodoManager()
manager.add_todo("Walk dog",True)
manager.add_todo("get milk",False)
print("*************")
print(manager.get_all())
print(manager.get_item("get milk"))
print(manager.get_item("get milk"))
         
todos=[]
todos.append({"id": 1, "task": "Buy milk", "done":False})
todos.append({"id": 2, "task": "Learn Python", "done":True})
print(todos)

value = "Buy milk"
for todo in todos:
    if todo["task"] == value:
        print(todo)
        break


for todo in todos:
    status="Done" if todo["done"] else "Pending"
    print(f"ID: {todo['id']}, Task: {todo['task']}, Status: {status}")

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
        if(self.marks>=35):
            return Pass
        else:
            return fail
result=Student()
result.display()