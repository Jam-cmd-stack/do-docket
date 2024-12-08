import sqlite3 

# Соединение с базой данных (если её нет, она создастся)
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Создание таблицы tasks
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT NOT NULL,
             description TEXT,
             status TEXT)''')

conn.commit()
conn.close()


def add_task(title, description, status="To Do"):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", (title, description, status))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[3]}")
    conn.close()

def update_task(task_id, status):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Основной цикл программы
while True:
    choice = input("Choose an action (add/view/update/delete/exit): ").lower()
    if choice == 'add':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        add_task(title, description)
    elif choice == 'view':
        view_tasks()
    elif choice == 'update':
        task_id = int(input("Enter task ID to update: "))
        new_status = input("Enter new status: ")
        update_task(task_id, new_status)
    elif choice == 'delete':
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == 'exit':
        break
    else:
        print("Invalid input, please try again.")
