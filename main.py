import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# ---------- DATABASE CONNECTION ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="office_visitor_db"
)
cursor = conn.cursor()

# ---------- CREATE TABLE ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    visitor_name VARCHAR(100),
    emp_id VARCHAR(50),
    entry_time VARCHAR(50)
)
""")

# ---------- FUNCTIONS ----------
def add_visitor():
    name = entry_name.get()
    emp_id = entry_emp.get()

    if name == "" or emp_id == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO visitors (visitor_name, emp_id, entry_time) VALUES (%s, %s, %s)",
        (name, emp_id, time)
    )
    conn.commit()

    messagebox.showinfo("Success", "Visitor added successfully!")
    clear_fields()
    load_data()

def load_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM visitors")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_emp.delete(0, tk.END)

# ---------- UI ----------
root = tk.Tk()
root.title("Office Visitor Management System")
root.geometry("900x500")
root.configure(bg="#1e1e2f")

# ---------- LEFT FRAME (FORM) ----------
frame_left = tk.Frame(root, bg="#1e1e2f")
frame_left.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(frame_left, text="Visitor Name", fg="white", bg="#1e1e2f").pack(anchor="w")
entry_name = tk.Entry(frame_left, width=25)
entry_name.pack(pady=5)

tk.Label(frame_left, text="Employee ID", fg="white", bg="#1e1e2f").pack(anchor="w")
entry_emp = tk.Entry(frame_left, width=25)
entry_emp.pack(pady=5)

tk.Button(frame_left, text="Add Visitor", width=20, command=add_visitor).pack(pady=10)
tk.Button(frame_left, text="Refresh List", width=20, command=load_data).pack(pady=5)
tk.Button(frame_left, text="Clear", width=20, command=clear_fields).pack(pady=5)

# ---------- RIGHT FRAME (TABLE) ----------
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=20, pady=20)

columns = ("ID", "Name", "Emp ID", "Entry Time")
tree = ttk.Treeview(frame_right, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack()

# ---------- LOAD DATA ----------
load_data()

root.mainloop()
